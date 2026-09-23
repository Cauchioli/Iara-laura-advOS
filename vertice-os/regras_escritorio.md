# Diretrizes de Governança & Configuração: Vértice OS (Iara & Laura)

## 1. Política de Acesso e Isolamento de Pastas (Google Drive)

### Pasta 01: DIRETORIA & SÓCIAS (Acesso Restrito)
* Caminho: `G:/Meu Drive/01_Diretoria_Financeiro/`
* Regra Vértice OS: **PROIBIDA A INDEXAÇÃO PELO RAG DAS ESTAGIÁRIAS.**
* Conteúdo: DRE, balanços, pró-labore, contratos sociais, faturamento e estratégias confidenciais.

### Pasta 02: OPERACIONAL ESCRITÓRIO (Acesso Compartilhado)
* Caminho: `G:/Meu Drive/02_Operacional_Processos/`
* Regra Vértice OS: **INDEXAÇÃO SEMÂNTICA TOTAL (RAG ATIVO).**
* Subpastas Monitoradas:
  - `01_Clientes/`: Pasta individual de cada cliente com documentos e transcrições de áudio.
  - `02_Banco_de_Teses/`: Petições aprovadas e modelos de referência do escritório (priorizar últimos 8 meses).
  - `03_Fila_Revisao/`: Local onde as estagiárias depositam as minutas geradas pela IA para conferência da Keren.

---

## 2. Divisão de Agentes & Skills Operacionais

### Agente 1: Elaborador Júnior (Estagiárias de Base)
* Operadoras: Maria Carolina e Stephany.
* Arquivo da Skill: `vertice-os/prompts/skill_elaboracao_estagiarias.md`.
* Função: Converter fatos, gravações e histórico na primeira minuta estruturada.
* Trava: Não envia para sócias; deposita na fila da Coordenadora Keren.

### Agente 2: Coordenadora de Revisão e Saneamento (Keren)
* Operadora: Keren (Estagiária Sênior / Coordenadora Técnica).
* Arquivo da Skill: `vertice-os/prompts/skill_revisao_estagiaria_king.md`.
* Função: Raio-X formal em até 5 minutos (endereçamento, folhas, artigos vigentes, anexos e regras de estilo).
* Trava: Libera apenas peças 100% saneadas para a supervisão sênior.

### Agente 3: Supervisão Estratégica & Deferimento (Dra. Laura / Dra. Iara)
* Operadoras: Dra. Laura Oliveira (e Dra. Iara durante a viagem aos EUA).
* Arquivo da Skill: `vertice-os/prompts/skill_revisao_laura.md`.
* Função: Avaliar tese jurídica, força persuasiva, preliminares e deferimento em até 3 minutos.
* Trava: Validação humana mandatória antes do protocolo judicial.

### Agente 4: Esteira Comercial e CRM (Ana & Nanda)
* Operadoras: Ana (SDR / Atendimento) e Nanda (Supervisora Comercial / Contratos Fechados).
* Arquivo da Skill: `vertice-os/prompts/skill_atendimento_comercial_nanda.md`.
* Função: Triagem de leads, cadência D+1, D+3, D+7 no Kanban do Astrea, script de quebra de objeções e passagem de bastão de contratos assinados.
