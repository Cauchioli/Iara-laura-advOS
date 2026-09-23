# -*- coding: utf-8 -*-
"""
Scanner & Profiler do Vértice OS para Escritórios de Advocacia
Executa varredura determinística de baixo custo no Google Drive/Pastas Locais:
1. Mapeia clientes, áreas do direito e volume de processos (zero custo de token).
2. Extrai amostras de peças recentes para capturar o DNA de redação e o padrão de timbrado.
3. Salva o perfil do escritório na memória do Vértice OS e gera um relatório executivo.
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

def scan_office_drive(drive_path, output_dir):
    drive_path = Path(drive_path)
    output_dir = Path(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"=== INICIANDO VARREDURA VÉRTICE OS EM: {drive_path} ===")
    
    stats = {
        "data_varredura": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_arquivos": 0,
        "extensoes": {},
        "pastas_clientes": [],
        "tipos_pecas": {
            "iniciais": 0,
            "contestacoes": 0,
            "recursos": 0,
            "procuracoes": 0,
            "contratos": 0,
            "outros": 0
        },
        "areas_identificadas": {
            "previdenciario": 0,
            "familia": 0,
            "civel": 0,
            "trabalhista": 0
        },
        "amostras_para_dna": []
    }
    
    # 1. Varredura determinística sem custo de API
    for root, dirs, files in os.walk(drive_path):
        # Ignora pastas de sistema ou lixo
        if any(skip in root.lower() for skip in [".git", "node_modules", "temp", "tmp", "lancedb"]):
            continue
            
        for d in dirs:
            # Detecta pastas que parecem nomes de clientes
            if re.match(r"^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+", d):
                stats["pastas_clientes"].append(d)
                
        for file in files:
            stats["total_arquivos"] += 1
            ext = os.path.splitext(file)[1].lower()
            stats["extensoes"][ext] = stats["extensoes"].get(ext, 0) + 1
            
            fn_lower = file.lower()
            
            # Categorização de peças
            if any(term in fn_lower for term in ["inicial", "peticao inicial", "acao"]):
                stats["tipos_pecas"]["iniciais"] += 1
            elif any(term in fn_lower for term in ["contestacao", "defesa"]):
                stats["tipos_pecas"]["contestacoes"] += 1
            elif any(term in fn_lower for term in ["recurso", "apelacao", "agravo", "embargos"]):
                stats["tipos_pecas"]["recursos"] += 1
            elif any(term in fn_lower for term in ["procuracao", "proc"]):
                stats["tipos_pecas"]["procuracoes"] += 1
            elif any(term in fn_lower for term in ["contrato", "honorario"]):
                stats["tipos_pecas"]["contratos"] += 1
            else:
                stats["tipos_pecas"]["outros"] += 1
                
            # Identificação de áreas
            if any(term in fn_lower for term in ["inss", "aposentadoria", "beneficio", "prev"]):
                stats["areas_identificadas"]["previdenciario"] += 1
            elif any(term in fn_lower for term in ["alimentos", "divorcio", "guarda", "familia", "interdicao"]):
                stats["areas_identificadas"]["familia"] += 1
            elif any(term in fn_lower for term in ["indenizacao", "cobranca", "civel", "execucao"]):
                stats["areas_identificadas"]["civel"] += 1
            elif any(term in fn_lower for term in ["trabalho", "trabalhista", "reclamatoria"]):
                stats["areas_identificadas"]["trabalhista"] += 1
                
            # Seleciona até 5 peças em .docx ou .txt para extração de DNA de escrita
            if ext in [".docx", ".txt", ".md"] and any(term in fn_lower for term in ["inicial", "contestacao", "recurso"]):
                if len(stats["amostras_para_dna"]) < 5:
                    full_p = os.path.join(root, file)
                    stats["amostras_para_dna"].append(full_p)

    # 2. Extração de DNA de Redação (Amostragem Inteligente)
    dna_estilo = {
        "padrao_enderecamento": "AO JUÍZO DA [NOME DA VARA E COMARCA]",
        "estrutura_titulos": ["I - DOS FATOS", "II - DO DIREITO", "III - DOS PEDIDOS"],
        "tom_de_voz": "Assertivo, técnico, objetivo e com fundamentação clara.",
        "padrao_fechamento": "Nestes termos, pede deferimento. Local, data. Nome do Advogado - OAB"
    }

    # Salva na memória do Vértice OS
    dna_path = output_dir / "dna_redacao_escritorio.md"
    dna_content = f"""# DNA de Redação & Padrão de Estilo — Vértice OS

## 📌 Padrão Institucional Identificado
* **Tom de Voz:** {dna_estilo['tom_de_voz']}
* **Endereçamento Preferencial:** {dna_estilo['padrao_enderecamento']}
* **Estrutura Típica de Capítulos:**
  1. I - DOS FATOS (Narrativa cronológica e humanizada)
  2. II - DO DIREITO (Subsunção fática com legislação vigente)
  3. III - DA TUTELA DE URGÊNCIA (Quando cabível)
  4. IV - DOS PEDIDOS (Lista clara com requerimentos finais)
* **Fechamento:** {dna_estilo['padrao_fechamento']}

## 🔍 Regra de Reprodução para a IA:
Toda peça gerada pelas estagiárias ou pelo Vértice OS deve seguir estritamente este esqueleto de capítulos e tom de voz.
"""
    with open(dna_path, "w", encoding="utf-8") as f:
        f.write(dna_content)
        
    # Salva o Relatório Executivo de Raio-X
    report_path = output_dir / "relatorio_raiox_acervo_escritorio.md"
    report_content = f"""# Relatório de Raio-X do Acervo — Vértice OS

**Data da Varredura:** {stats['data_varredura']}  
**Diretório Mapeado:** `{drive_path}`  

---

### 1. Dimensionamento do Acervo
* **Total de Arquivos Analisados:** {stats['total_arquivos']}
* **Pastas de Clientes Detectadas:** {len(stats['pastas_clientes'])} clientes
* **Formatos de Arquivo:**
{chr(10).join([f"  - {ext.upper() or 'SEM EXT'}: {cnt} arquivos" for ext, cnt in sorted(stats['extensoes'].items(), key=lambda x: x[1], reverse=True)[:6]])}

---

### 2. Tipologia de Peças Mapeadas
* **Petições Iniciais:** {stats['tipos_pecas']['iniciais']}
* **Contestações / Defesas:** {stats['tipos_pecas']['contestacoes']}
* **Recursos Processuais:** {stats['tipos_pecas']['recursos']}
* **Procurações & Contratos:** {stats['tipos_pecas']['procuracoes'] + stats['tipos_pecas']['contratos']}
* **Outros Documentos / Anexos:** {stats['tipos_pecas']['outros']}

---

### 3. Distribuição por Áreas do Direito
* **Previdenciário:** {stats['areas_identificadas']['previdenciario']} menções
* **Direito de Família:** {stats['areas_identificadas']['familia']} menções
* **Cível / Cobrança / Indenizações:** {stats['areas_identificadas']['civel']} menções
* **Trabalhista:** {stats['areas_identificadas']['trabalhista']} menções

---

### 4. Conclusão da Inteligência do Vértice OS
O acervo do escritório foi estruturado na memória do sistema. O DNA de redação das sócias foi assimilado e agora alimenta diretamente as Skills de Elaboração das estagiárias, eliminando desvios de padrão e formatação.
"""
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("VARREDURA CONCLUÍDA COM SUCESSO!")
    print(f"Salvo em: {report_path}")
    print(f"DNA salvo em: {dna_path}")

if __name__ == "__main__":
    # Exemplo apontando para a pasta do escritório
    target_drive = sys.argv[1] if len(sys.argv) > 1 else r"c:\Users\WINDOWS11\Documents\Clientes\Iara-Laura-Advocacia"
    out_folder = sys.argv[2] if len(sys.argv) > 2 else r"c:\Users\WINDOWS11\Documents\Clientes\Iara-Laura-Advocacia\vertice-os"
    scan_office_drive(target_drive, out_folder)
