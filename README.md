# Vértice OS: Infraestrutura Operacional & Inteligência Jurídica
## Cliente: Iara & Laura Advocacia

Repositório unificado da infraestrutura de inteligência operacional do escritório Iara & Laura Advocacia, estruturado pela Vértice OS.
Este sistema unifica as diretrizes de produção de peças processuais, o saneamento formal da controladoria técnica e a esteira de atendimento comercial.

---

## 1. Visão Geral da Arquitetura

O sistema opera sob duas esteiras principais integradas:

### A. Esteira Jurídica em 3 Níveis
1. Nível 01 (Elaboração Base): Maria Carolina e Stephany produzem a primeira minuta orientada ao objetivo macro da demanda.
2. Nível 02 (Saneamento e Conformidade): Keren realiza o raio-X formal, documental e processual em até 5 minutos.
3. Nível 03 (Supervisão Estratégica): Dra. Laura Oliveira e Dra. Iara Viana auditam mérito, tese substantiva e deferimento em até 3 minutos.

### B. Esteira Comercial & CRM
1. Triagem & Pré-lead: Ana (SDR) qualifica contatos, aplica a regra de descarte no WhatsApp e cadastra no Astrea.
2. Cadência de Agendamento: Acompanhamento em D+1, D+3 e D+7, consulta fixada a R$ 400,00 e quebra de objeções.
3. Passagem de Bastão: Contrato assinado gera automaticamente a tarefa "Gestão de Contrato Fechado" para a Nanda.

---

## 2. Estrutura do Repositório

```text
├── 1-contexto/                 # Perfil institucional, histórico e mapeamento da equipe
├── 2-deliverables/             # Relatórios executivos, propostas e cronogramas
├── 3-reunioes/                 # Atas executivas e alinhamentos operacionais
├── vertice-os/                 # Núcleo técnico do sistema operacional
│   ├── _memoria/               # Memória contextual persistente
│   ├── prompts/                # As 4 Skills em Markdown
│   │   ├── skill_elaboracao_estagiarias.md
│   │   ├── skill_revisao_estagiaria_king.md
│   │   ├── skill_revisao_laura.md
│   │   └── skill_atendimento_comercial_nanda.md
│   ├── dna_redacao_escritorio.md
│   ├── regras_escritorio.md
│   └── scanner_onboarding_drive.py
├── AGENTS.md                   # Governança operacional universal para agentes de IA
├── CLAUDE.md                   # Instruções nativas para Claude Code e Claude Projects
├── GEMINI.md                   # Instruções nativas para Antigravity e ecossistema Gemini
├── setup_vertice_os.bat        # Instalador rápido para Windows
└── setup_vertice_os.ps1        # Script de inicialização em PowerShell
```

---

## 3. Guia de Instalação e Ativação

O projeto foi construído para instalação transparente em qualquer estação de trabalho (notebook da Dra. Iara, notebook da Dra. Laura ou computadores da equipe).

### Opção 1: Instalação via Antigravity / Gemini CLI
1. Clone o repositório na pasta local de trabalho:
   ```bash
   git clone https://github.com/SEU-USUARIO/iara-laura-advocacia.git
   ```
2. Abra a pasta no terminal ou no Antigravity:
   ```bash
   cd iara-laura-advocacia
   ```
3. O Antigravity carregará automaticamente o arquivo `AGENTS.md` e as skills disponíveis no diretório.

### Opção 2: Instalação via Claude Code ou Claude Desktop / Projects
1. Clone o repositório na máquina:
   ```bash
   git clone https://github.com/SEU-USUARIO/iara-laura-advocacia.git
   ```
2. O Claude Code reconhecerá automaticamente o arquivo `CLAUDE.md` na raiz do projeto.
3. Para uso no Claude Web (Claude Projects):
   - Crie um novo projeto no Claude chamado "Iara & Laura Advocacia".
   - No campo "System Prompt / Instructions", cole o conteúdo de `CLAUDE.md` ou da skill específica do posto de trabalho.
   - Na aba "Project Knowledge", adicione os arquivos `dna_redacao_escritorio.md`, `regras_escritorio.md` e os arquivos de prompt correspondentes.

### Opção 3: Execução do Scanner de Acervo do Google Drive
Para mapear o acervo histórico sem custo de tokens:
```bash
python vertice-os/scanner_onboarding_drive.py "G:\Meu Drive\02_Operacional_Processos" "vertice-os"
```

---

## 4. Diretrizes Invioláveis de Segurança e Estilo
* Sigilo Absoluto: Pastas financeiras e societárias permanecem estritamente isoladas e inacessíveis para agentes e colaboradores.
* Proibição de Vocabulário Específico: Vedado o uso do termo "menor" (utilizar criança, adolescente, filho ou filha) e da expressão "o mesmo".
* Sem Travessões como Separadores: Utilizar vírgulas, dois-pontos ou parênteses.
* Validação Humana Mandatória: Todas as petições passam por conferência da Keren e validação final da Dra. Laura ou Dra. Iara antes do protocolo judicial.
