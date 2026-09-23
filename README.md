# Vértice OS: Segundo Cérebro Jurídico & Comercial
## Cliente: Iara & Laura Advocacia

Repositório unificado da infraestrutura de inteligência operacional e Segundo Cérebro do escritório Iara & Laura Advocacia.
Estruturado sob a metodologia Vértice OS (Vault Markdown em padrão Johnny Decimal / PARA), este sistema transforma o acervo do escritório em uma base de conhecimento leve, pesquisável e de altíssima eficiência de tokens para agentes de IA (Claude, Antigravity, NotebookLM).

---

## 1. Princípio Fundamental: Converta UMA Vez, Consulte Infinitas Vezes

* **O Google Drive guarda a prova documental:** Arquivos brutos (PDFs de 80 páginas, DOCXs, áudios) permanecem onde estão, intocáveis em suas pastas de origem.
* **O Segundo Cérebro guarda a memória ativa:** A esteira de conversão processa cada arquivo relevante uma única vez, gerando uma nota Markdown leve (15 KB) com cabeçalho YAML padronizado.
* **Economia Real:** As consultas da inteligência artificial passam a consumir 2.000 a 4.000 tokens por análise (em vez de queimar 50.000 a 100.000 tokens relendo arquivos brutos a cada conversa), com 90% a 95% de economia permanente.

---

## 2. Mapa Decimal do Vault (Johnny Decimal)

```text
Iara-laura-advOS/
├── 00-ENTRADA.md                    # Visão panorâmica e porta de entrada do escritório
├── 01-REGRAS.md                     # Governança inegociável, estilo e blindagem de segurança
├── 02-PROTOCOLO-ORGANIZADOR.md      # Protocolo para organização do Drive com lacre
├── 03-SCHEMA.md                     # Especificação dos campos e metadados YAML das notas
├── 10-clientes/                     # Fichas e resumos de casos dos clientes ativos
├── 20-modelos/                      # Peças padrão ouro da Dra. Laura convertidas em .md
├── 30-teses/                        # Banco de teses e jurisprudências validadas
├── 40-operacional/                  # Manuais de rotina, CRM do Astrea e scripts
│   ├── crm_comercial_astrea.md      # As 7 fases do Kanban e cadência D+1, D+3, D+7
│   └── prompts/                     # As 4 Skills Operacionais parametrizadas
│       ├── 01_skill_elaboracao_estagiarias.md
│       ├── 02_skill_revisao_coordenacao_keren.md
│       ├── 03_skill_supervisao_laura_iara.md
│       └── 04_skill_comercial_crm_ana_nanda.md
├── 90-transcricoes/                 # Memória das reuniões e instruções gravadas
├── AGENTS.md                        # Governança universal para Antigravity e Gemini
├── CLAUDE.md                        # Instruções nativas para Claude Code e Claude Projects
├── GEMINI.md                        # Diretrizes do ecossistema Gemini
└── scripts/
    ├── converter_drive_para_vault.py  # Conversor determinístico Drive -> Vault
    ├── rag_escritorio.py              # Indexador semântico local com blindagem
    ├── setup_vertice_os.bat           # Instalador Windows com 1 clique
    └── setup_vertice_os.ps1           # Script de setup em PowerShell
```

---

## 3. As 4 Skills do Ecossistema em `40-operacional/prompts/`

1. `01_skill_elaboracao_estagiarias.md`: Nível 1 (Elaboração pelas estagiárias de base com foco no objetivo macro da demanda).
2. `02_skill_revisao_coordenacao_keren.md`: Nível 2 (Saneamento formal e probatório pela Keren em até 5 minutos).
3. `03_skill_supervisao_laura_iara.md`: Nível 3 (Supervisão técnica sênior de tese e deferimento pela Dra. Laura ou Dra. Iara em até 3 minutos).
4. `04_skill_comercial_crm_ana_nanda.md`: Esteira Comercial (Kanban de 7 fases no Astrea, filtro de Pré-lead e quebra de objeções para Ana e Nanda).

---

## 4. Guia Rápido de Instalação e Conversão do Drive

### Passo 1: Clonar o Repositório
No computador da Dra. Iara ou da equipe:
```bash
git clone https://github.com/Cauchioli/Iara-laura-advOS.git
cd Iara-laura-advOS
```

### Passo 2: Executar o Conversor para o Google Drive
Para converter as peças e modelos da pasta operacional do Google Drive em notas Markdown leves:
```bash
python scripts/converter_drive_para_vault.py "G:\Meu Drive\escritorio oliveira viana"
```
*(As pastas de diretoria e financeiro serão terminantemente ignoradas pela regra de blindagem).*

### Passo 3: Ativação no Claude ou Antigravity
* No Claude Code: execute `claude` na raiz do projeto. O `CLAUDE.md` carregará automaticamente todo o ecossistema.
* No Claude Projects: adicione `CLAUDE.md` nas instruções e anexe as notas convertidas e as skills em Project Knowledge.
* No Antigravity: abra a pasta do repositório. O `AGENTS.md` guiará todas as operações.
