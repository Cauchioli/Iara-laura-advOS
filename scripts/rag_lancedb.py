# -*- coding: utf-8 -*-
"""
RAG Local em LanceDB: Vertice OS & Segundo Cerebro
Cliente: Iara e Laura Advocacia

Motor de busca vetorial leve e embarcado:
- Banco de dados vetorial: LanceDB (persistente em disco local, sem nuvem, sem servidor).
- Embeddings: sentence-transformers (intfloat/multilingual-e5-small, leve e otimizado para portugues em CPU).
- Seguranca e Sigilo: Blindagem automatica que impede leitura de pastas financeiras e societarias.
"""

import os
import sys
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

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = str(BASE_DIR / "lancedb")
MANIFEST_PATH = str(BASE_DIR / "manifest_lancedb.json")
TABLE_NAME = "acervo_juridico"
MODEL_NAME = "intfloat/multilingual-e5-small"
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
BATCH_SIZE = 16

DOC_EXTENSIONS = {".md", ".docx", ".pdf", ".txt"}
SKIP_EXTENSIONS = {".exe", ".rar", ".zip", ".7z", ".png", ".jpg", ".jpeg", ".gif", ".bak", ".tmp", ".mp4", ".mp3", ".xlsx"}

SKIP_DIRECTORIES = re.compile(
    r"[\\/](01_Diretoria[^\\/]*|financeiro[^\\/]*|contabil[^\\/]*|societario[^\\/]*|prolabore[^\\/]*|\.git|\.venv|venv|node_modules|lancedb|__pycache__)([\\/]|$)",
    re.I
)

def extract_content(file_path, ext):
    try:
        if ext == ".md" or ext == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        elif ext == ".docx":
            import docx
            doc = docx.Document(file_path)
            return "\n\n".join(p.text for p in doc.paragraphs if p.text.strip())
        elif ext == ".pdf":
            import pdfplumber
            pages = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text() or ""
                    if text.strip():
                        pages.append(text)
            return "\n\n".join(pages)
    except Exception as exc:
        print(f"[AVISO] Falha ao ler {file_path}: {exc}")
    return ""

def split_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if len(chunk) > 40:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

_embedding_model = None
def load_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            print(f"[RAG] Carregando modelo leve de embedding ({MODEL_NAME})...")
            _embedding_model = SentenceTransformer(MODEL_NAME, device="cpu")
            try:
                _embedding_model.max_seq_length = 384
            except Exception:
                pass
            print("[RAG] Modelo carregado com sucesso na CPU.")
        except ImportError:
            print("[ERRO] Pacote sentence-transformers nao instalado.")
            print("Execute no terminal: pip install sentence-transformers lancedb")
            sys.exit(1)
    return _embedding_model

def generate_embeddings(text_list, prefix="passage"):
    model = load_embedding_model()
    prepared_texts = [f"{prefix}: {t}" for t in text_list]
    for bs in (BATCH_SIZE, 8, 4, 1):
        try:
            return model.encode(
                prepared_texts,
                normalize_embeddings=True,
                batch_size=bs,
                show_progress_bar=False
            ).tolist()
        except RuntimeError as exc:
            if "memory" in str(exc).lower() and bs > 1:
                continue
            raise

def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_manifest(manifest):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

def command_index(roots, reset=False):
    try:
        import lancedb
    except ImportError:
        print("[ERRO] Pacote lancedb nao instalado.")
        print("Execute no terminal: pip install lancedb sentence-transformers")
        return

    if reset and os.path.exists(DB_DIR):
        import shutil
        shutil.rmtree(DB_DIR, ignore_errors=True)
        if os.path.exists(MANIFEST_PATH):
            os.remove(MANIFEST_PATH)
        print("[RESET] Indice vetorial LanceDB zerado.")

    db = lancedb.connect(DB_DIR)
    manifest = load_manifest()

    if not roots:
        # Por padrao, indexa o Vault do Segundo Cerebro
        roots = [
            str(BASE_DIR / "10-clientes"),
            str(BASE_DIR / "20-modelos"),
            str(BASE_DIR / "30-teses"),
            str(BASE_DIR / "40-operacional")
        ]

    candidate_files = []
    for r in roots:
        if not os.path.exists(r):
            continue
        for root, dirs, files in os.walk(r):
            if SKIP_DIRECTORIES.search(root):
                continue
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in DOC_EXTENSIONS and ext not in SKIP_EXTENSIONS:
                    candidate_files.append((os.path.join(root, file), ext))

    print(f"=== INICIANDO INDEXACAO VETORIAL NO LANCEDB ===")
    print(f"Arquivos identificados: {len(candidate_files)}")

    new_chunks = []
    processed_files = 0
    skipped_files = 0

    for path, ext in candidate_files:
        try:
            mtime = os.path.getmtime(path)
            size = os.path.getsize(path)
        except OSError:
            continue

        if path in manifest and abs(manifest[path].get("mtime", 0) - mtime) < 1:
            skipped_files += 1
            continue

        if size > 15 * 1024 * 1024:
            print(f"[AVISO] Arquivo muito grande ignorado (>15MB): {os.path.basename(path)}")
            continue

        text = extract_content(path, ext)
        chunks = split_into_chunks(text)
        if not chunks:
            manifest[path] = {"mtime": mtime, "chunks": 0}
            continue

        vectors = generate_embeddings(chunks, prefix="passage")
        for idx, (chunk, vec) in enumerate(zip(chunks, vectors)):
            new_chunks.append({
                "id": hashlib.md5(f"{path}_{idx}".encode("utf-8")).hexdigest(),
                "vector": vec,
                "text": chunk,
                "file_path": path,
                "file_name": os.path.basename(path),
                "chunk_idx": idx,
                "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
            })

        manifest[path] = {"mtime": mtime, "chunks": len(chunks)}
        processed_files += 1

    if new_chunks:
        if TABLE_NAME in db.table_names():
            table = db.open_table(TABLE_NAME)
            table.add(new_chunks)
        else:
            table = db.create_table(TABLE_NAME, data=new_chunks)
        print(f"[OK] {len(new_chunks)} novos chunks vetorizados e inseridos no LanceDB.")
    else:
        print("[INFO] Nenhum documento novo ou alterado para indexar.")

    save_manifest(manifest)
    print(f"Indexacao concluida: {processed_files} processados, {skipped_files} inalterados.")

def command_query(query_text, top_k=5):
    try:
        import lancedb
    except ImportError:
        print("[ERRO] Pacote lancedb nao instalado.")
        return

    if not os.path.exists(DB_DIR):
        print("[AVISO] Banco de dados LanceDB ainda nao foi criado. Execute 'index' primeiro.")
        return

    db = lancedb.connect(DB_DIR)
    if TABLE_NAME not in db.table_names():
        print("[AVISO] Tabela de documentos vazia. Execute 'index' primeiro.")
        return

    table = db.open_table(TABLE_NAME)
    query_vector = generate_embeddings([query_text], prefix="query")[0]
    results = table.search(query_vector).limit(top_k).to_list()

    print(f"=== RESULTADOS DA BUSCA SEMANTICA (LANCEDB) ===")
    print(f"Consulta: '{query_text}'")
    print(f"Documentos recuperados: {len(results)}\n")

    for i, res in enumerate(results, 1):
        dist = res.get("_distance", 0.0)
        score = max(0.0, 1.0 - dist)
        print(f"[{i}] {res['file_name']} (Similaridade: {score:.3f})")
        print(f"    Origem: {res['file_path']}")
        clean_excerpt = res['text'][:250].replace("\n", " ")
        print(f"    Trecho: \"{clean_excerpt}...\"\n")

def command_stats():
    try:
        import lancedb
        if os.path.exists(DB_DIR):
            db = lancedb.connect(DB_DIR)
            if TABLE_NAME in db.table_names():
                table = db.open_table(TABLE_NAME)
                print(f"Tabela LanceDB '{TABLE_NAME}': {len(table)} chunks indexados.")
            else:
                print("Tabela ainda nao criada.")
        else:
            print("Diretorio LanceDB inexistente.")
    except Exception as exc:
        print(f"Status do LanceDB: {exc}")

    manifest = load_manifest()
    print(f"Manifesto de Documentos: {len(manifest)} arquivos mapeados.")

def main():
    parser = argparse.ArgumentParser(description="RAG Local em LanceDB: Vertice OS")
    subparsers = parser.add_subparsers(dest="command")

    p_index = subparsers.add_parser("index", help="Indexa o Vault ou pastas do Google Drive")
    p_index.add_argument("roots", nargs="*", help="Pastas para indexar (padrao: Vault local)")
    p_index.add_argument("--reset", action="store_true", help="Recria o indice vetorial do zero")

    p_query = subparsers.add_parser("query", help="Consulta semantica de teses e pecas")
    p_query.add_argument("text", help="Pergunta ou tema de pesquisa")
    p_query.add_argument("-k", type=int, default=5, help="Quantidade de resultados")

    subparsers.add_parser("stats", help="Exibe estatisticas do banco vetorial")

    args = parser.parse_args()
    if args.command == "index":
        command_index(args.roots, reset=args.reset)
    elif args.command == "query":
        command_query(args.text, top_k=args.k)
    elif args.command == "stats":
        command_stats()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
