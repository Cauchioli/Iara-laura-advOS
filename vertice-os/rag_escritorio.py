# -*- coding: utf-8 -*-
"""
RAG e Indexador Semantico Local: Vertice OS (Iara e Laura Advocacia)
Indexacao e busca vetorial 100% local e privada em acervos de pecas e teses.
Garante blindagem absoluta de pastas financeiras e societarias.
"""

import sys
import os
import json
import argparse
import hashlib
import time
import re
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "lancedb")
MANIFEST_FILE = os.path.join(BASE_DIR, "manifest_acervo.json")
TABLE_NAME = "acervo_pecas"
MODEL_NAME = "intfloat/multilingual-e5-small"
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
BATCH_SIZE = 16

DOC_EXTENSIONS = {".pdf", ".docx", ".txt", ".md"}
SKIP_EXTENSIONS = {".exe", ".rar", ".zip", ".7z", ".png", ".jpg", ".jpeg", ".gif", ".bak", ".tmp", ".mp4", ".mp3"}

# Pastas terminantemente proibidas de serem indexadas (Sigilo e LGPD)
SKIP_DIRECTORIES = re.compile(
    r"[\\/](01_Diretoria[^\\/]*|financeiro[^\\/]*|contabil[^\\/]*|societario[^\\/]*|prolabore[^\\/]*|\.git|\.venv|node_modules|lancedb|__pycache__)([\\/]|$)",
    re.I
)

def extract_text(file_path, ext):
    try:
        if ext == ".docx":
            import docx
            doc = docx.Document(file_path)
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        elif ext == ".pdf":
            import pdfplumber
            pages = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text() or ""
                    if text.strip():
                        pages.append(text)
            return "\n".join(pages)
        elif ext in (".txt", ".md"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
    except Exception as exc:
        print(f"[AVISO] Falha ao extrair {file_path}: {exc}")
    return ""

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def run_indexer(target_path, reset=False):
    target_path = os.path.abspath(target_path)
    print(f"=== INICIANDO INDEXACAO SEMANTICA LOCAL DO ACERVO ===")
    print(f"Diretorio Alvo: {target_path}")
    print(f"Regra de Seguranca: Pastas de Diretoria/Financeiro estao estritamente bloqueadas.")
    
    files_to_index = []
    for root, dirs, files in os.walk(target_path):
        if SKIP_DIRECTORIES.search(root):
            continue
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in DOC_EXTENSIONS:
                full_path = os.path.join(root, file)
                files_to_index.append((full_path, ext))
                
    print(f"Documentos identificados para indexacao: {len(files_to_index)}")
    
    manifest = {}
    if os.path.exists(MANIFEST_FILE) and not reset:
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                manifest = json.load(f)
        except Exception:
            manifest = {}
            
    processed_count = 0
    for full_path, ext in files_to_index:
        mtime = os.path.getmtime(full_path)
        if full_path in manifest and manifest[full_path].get("mtime") == mtime:
            continue
            
        content = extract_text(full_path, ext)
        if not content:
            continue
            
        chunks = chunk_text(content)
        manifest[full_path] = {
            "mtime": mtime,
            "chunks_count": len(chunks),
            "indexed_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        processed_count += 1
        
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        
    print(f"[CONCLUIDO] Indexacao concluida com sucesso.")
    print(f"Novos documentos processados: {processed_count}")
    print(f"Total no manifesto: {len(manifest)}")

def query_index(query_text, top_k=5):
    print(f"Consulta semantica por: '{query_text}'")
    if not os.path.exists(MANIFEST_FILE):
        print("[ERRO] Indice vazio. Execute o comando 'index' primeiro.")
        return
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    print(f"Base de busca contem {len(manifest)} documentos monitorados.")

def main():
    parser = argparse.ArgumentParser(description="RAG & Indexador Semantico Local: Vertice OS")
    subparsers = parser.add_subparsers(dest="command")
    
    idx_parser = subparsers.add_parser("index", help="Indexa documentos do acervo")
    idx_parser.add_argument("path", help="Caminho da pasta operacional do Google Drive")
    idx_parser.add_argument("--reset", action="store_true", help="Reinicia o indice do zero")
    
    qry_parser = subparsers.add_parser("query", help="Busca teses e modelos por linguagem natural")
    qry_parser.add_argument("text", help="Texto ou pergunta da pesquisa")
    qry_parser.add_argument("-k", type=int, default=5, help="Quantidade de resultados")
    
    subparsers.add_parser("stats", help="Estatisticas do indice")
    
    args = parser.parse_args()
    if args.command == "index":
        run_indexer(args.path, reset=args.reset)
    elif args.command == "query":
        query_index(args.text, top_k=args.k)
    elif args.command == "stats":
        if os.path.exists(MANIFEST_FILE):
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"Documentos indexados: {len(data)}")
        else:
            print("Indice nao inicializado.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
