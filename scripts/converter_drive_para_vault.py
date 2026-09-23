# -*- coding: utf-8 -*-
"""
Conversor Determinístico: Google Drive para Vault Segundo Cérebro (Vértice OS)
Princípio: Converta UMA vez. Consulte infinitas vezes.

Varre a pasta operacional do Google Drive ("escritório oliveira viana") e gera
notas Markdown leves no padrão do Segundo Cérebro (com frontmatter YAML).
Blindagem absoluta: Pastas financeiras e societárias são terminantemente ignoradas.
"""

import os
import sys
import re
import json
import hashlib
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
CLIENTES_DIR = BASE_DIR / "10-clientes"
MODELOS_DIR = BASE_DIR / "20-modelos"
MANIFEST_FILE = BASE_DIR / "manifest_vault.json"

DOC_EXTENSIONS = {".docx", ".pdf", ".txt", ".md"}

# Pastas terminantemente proibidas de leitura e conversão (Sigilo e LGPD)
SKIP_DIRECTORIES = re.compile(
    r"[\\/](01_Diretoria[^\\/]*|financeiro[^\\/]*|contabil[^\\/]*|societario[^\\/]*|prolabore[^\\/]*|\.git|\.venv|node_modules|lancedb|__pycache__)([\\/]|$)",
    re.I
)

def extract_content(file_path, ext):
    try:
        if ext == ".docx":
            import docx
            doc = docx.Document(file_path)
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            return "\n\n".join(paragraphs)
        elif ext == ".pdf":
            import pdfplumber
            pages = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text() or ""
                    if text.strip():
                        pages.append(text)
            return "\n\n".join(pages)
        elif ext in (".txt", ".md"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
    except Exception as exc:
        print(f"[AVISO] Nao foi possivel extrair {file_path}: {exc}")
    return ""

def clean_filename(name):
    clean = re.sub(r"[^\w\s-]", "", name, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "_", clean).strip("_").lower()

def run_conversion(drive_path):
    drive_path = Path(drive_path).resolve()
    print("=== INICIANDO CONVERSAO DRIVE -> VAULT SEGUNDO CEREBRO ===")
    print(f"Diretorio Alvo no Drive: {drive_path}")
    print("Regra de Seguranca: Pastas de Diretoria e Financeiro estao bloqueadas.")
    
    CLIENTES_DIR.mkdir(parents=True, exist_ok=True)
    MODELOS_DIR.mkdir(parents=True, exist_ok=True)
    
    manifest = {}
    if MANIFEST_FILE.exists():
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                manifest = json.load(f)
        except Exception:
            manifest = {}

    converted_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(drive_path):
        if SKIP_DIRECTORIES.search(root):
            continue
            
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in DOC_EXTENSIONS:
                full_path = Path(root) / file
                file_str = str(full_path)
                mtime = os.path.getmtime(full_path)
                
                # Se ja foi convertido e nao mudou, pula (Economia de tokens e processamento)
                if file_str in manifest and manifest[file_str].get("mtime") == mtime:
                    skipped_count += 1
                    continue
                    
                content = extract_content(full_path, ext)
                if not content.strip():
                    continue
                    
                # Classificacao simples de destino
                fn_lower = file.lower()
                is_modelo = any(term in fn_lower for term in ["modelo", "padrao", "banco", "tese"])
                target_dir = MODELOS_DIR if is_modelo else CLIENTES_DIR
                
                safe_name = clean_filename(Path(file).stem) + ".md"
                dest_file = target_dir / safe_name
                
                # Geracao do Frontmatter YAML (Padrao Vertice OS)
                tipo = "modelo" if is_modelo else "caso"
                rel_path = str(full_path.relative_to(drive_path) if drive_path in full_path.parents else full_path)
                
                note_content = f"""---
tipo: {tipo}
titulo: "{file}"
fonte_drive: "{rel_path}"
convertido_em: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
formato_original: "{ext}"
status: ativo
---

# {file}

> [FONTE NO GOOGLE DRIVE]: `{full_path}`

{content}
"""
                with open(dest_file, "w", encoding="utf-8") as f:
                    f.write(note_content)
                    
                manifest[file_str] = {
                    "mtime": mtime,
                    "vault_note": str(dest_file.relative_to(BASE_DIR)),
                    "converted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                converted_count += 1

    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("=== CONVERSAO CONCLUIDA COM SUCESSO ===")
    print(f"Novas notas geradas no Vault: {converted_count}")
    print(f"Arquivos ja atualizados (pulados): {skipped_count}")
    print(f"Total monitorado no manifesto: {len(manifest)}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else r"G:\Meu Drive\escritorio oliveira viana"
    run_conversion(target)
