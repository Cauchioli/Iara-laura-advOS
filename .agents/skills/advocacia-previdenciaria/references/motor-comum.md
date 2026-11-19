# Motor Comum — Núcleo Metodológico

*Carregado em toda sessão, independente da área de prática.*

---

## Conteúdo

- [0. ANTI-ALUCINAÇÃO JURÍDICA — REGRA UNIVERSAL](#0-anti-alucinação-jurídica--regra-universal)
- [1. WORKFLOW SEQUENCIAL — TRÊS FLUXOS](#1-workflow-sequencial--três-fluxos)
- [2. INTAKE — EXTRAÇÃO ESTRUTURADA](#2-intake--extração-estruturada)
- [3. MAPA BRUTO — QUADRANTE PADRÃO](#3-mapa-bruto--quadrante-padrão)
- [4. AVALIAÇÃO DE RISCO](#4-avaliação-de-risco)
- [5. ARQUITETURA DA PEÇA](#5-arquitetura-da-peça)
- [6. PADRÃO DE REDAÇÃO](#6-padrão-de-redação)
- [7. CHECKLIST DE REVISÃO — TRANSVERSAL](#7-checklist-de-revisão--transversal)
- [8. GATE ANTI-PULO-DE-MAPA](#8-gate-anti-pulo-de-mapa)
- [9. CASOS HÍBRIDOS](#9-casos-híbridos)

---

## 0. ANTI-ALUCINAÇÃO JURÍDICA — REGRA UNIVERSAL

*Precede o workflow. Aplica-se a toda saída, em qualquer modo, para qualquer área. Não é opcional, não admite exceção.*

### 0.0 Princípio

O argumento em prosa segura é sempre preferível ao número fictício. A peça que cita precedente inventado perde credibilidade inteira — não só o argumento que o usa. A peça que usa prosa genérica bem fundamentada é defensável.

**Mas atenção:** o princípio não autoriza evitar jurisprudência por preguiça de pesquisar. A regra completa:

> **"Prosa segura é preferível ao número fictício — mas busca ativa de precedente verificável é preferível à prosa segura."**

Quando a tese se beneficia de ancoragem em precedente e o precedente é localizável via web_search ou base interna, é dever do mapa identificar isso e executar a busca antes de fechar a peça. Ver `references/pesquisa-jurisprudencial.md` — obrigatório em MINUTA e REVISÃO.

**Modo de falha que esta calibragem corrige:** peça com arquitetura sólida invoca um "princípio consolidado" (ex.: "o tempo especial sempre se converte", "a qualidade de segurado se mantém indefinidamente") quando há Tema do STJ ou Súmula da TNU que mitiga ou condiciona o requisito. A omissão não é de rigor — é de pesquisa não realizada. Em previdenciário, invocar princípio sem verificar o Tema/Súmula vinculante é o modo de falha mais comum.

Este protocolo define condutas obrigatórias, não recomendações.

### 0.1 Hierarquia de confiabilidade

**Nível 1 — SEGURO (pode citar com número):**

| Fonte | Condição |
|---|---|
| Precedente extraído de documento do caso | Número e ementa verificados no documento |
| Súmula Vinculante do STF | Número e texto conferidos |
| Súmula do STJ / da TNU com texto conferido | Verificar se não foi cancelada ou revisada |
| Tema de repercussão geral STF / recurso repetitivo STJ / representativo TNU | Número e tese confirmados em portal oficial |
| Dispositivo de lei/EC em texto consolidado | Conferir redação vigente na data de referência |

**Nível 2 — USO COM RESSALVA (citar com sinalização):**

| Situação | Conduta |
|---|---|
| Número mencionado pelo usuário, não verificado em documento | *[VERIFICAR ANTES DE PROTOCOLAR — não confirmado]* |
| Súmula/Tema que o usuário menciona sem enviar o texto | *[VERIFICAR TEXTO/STATUS ATUAL]* |
| IN INSS citada por número sem confirmar vigência | *[VERIFICAR IN VIGENTE NA DER]* |

**Nível 3 — PROIBIDO (nunca citar com número):**

| Situação | Conduta obrigatória |
|---|---|
| Número gerado por inferência do treinamento | Prosa genérica — nunca o número |
| Tema/REsp/Súmula que "parece existir" | Prosa genérica |
| Ementa reconstituída de memória | Não usar — nem com ressalva |
| Relator, data ou turma inferidos | Não mencionar sem verificação |

### 0.2 Prosa genérica — como usar

Quando o argumento é sólido mas o precedente não foi verificado:

> "O Superior Tribunal de Justiça tem decidido reiteradamente que..."
> "A jurisprudência consolidada da Turma Nacional de Uniformização reconhece que..."
> "O Supremo Tribunal Federal, em sede de repercussão geral, firmou o entendimento de que..."

**Regra:** prosa genérica jamais inventa; apenas afirma uma tendência sem atribuir decisão específica inexistente.

### 0.3 Controle de dados e fatos

| Tipo | Conduta |
|---|---|
| Valor (RMI, atrasados, salário-de-contribuição) | Só citar com documento ou cálculo verificável |
| Data (DER, DIB, DCB, DII, DID, óbito, filiação) | Conferir no documento/CNIS antes de inserir |
| Tempo de contribuição / carência | Calcular sobre o CNIS conferido; nunca afirmar de memória |
| Percentual / coeficiente / fator | Citar com fonte (lei, EC, tabela do ano) |
| Teto e salário mínimo | Valor anual — *[VERIFICAR valor do ano de referência]* |

Inferência sinalizada: "Estima-se que..." + *(dado a confirmar antes do protocolo)*. Nunca apresentar inferência como fato.

### 0.4 Controle de normas

Verificar antes de citar número de artigo:

| Norma | Risco |
|---|---|
| Lei 8.213/91 / 8.212/91 | Múltiplas alterações pós-EC 103 — conferir redação vigente na data de referência |
| Decreto 3.048/99 (RPS) | Alterado por decretos sucessivos — conferir |
| IN INSS | Substituídas com frequência — confirmar a vigente na DER e a atual |
| EC 103/2019 | Regras de transição e permanentes — não confundir com regra anterior (direito adquirido pré-reforma) |
| Súmulas TNU/STJ | Cancelamentos e revisões — verificar texto atual |

**Regra temporal (tempus regit actum):** o direito ao benefício rege-se, em princípio, pela lei vigente na data do fato gerador (DER, óbito, DII). Norma posterior mais favorável não retroage salvo previsão expressa; norma anterior revogada continua aplicável ao direito adquirido. Nunca escolher a norma sem antes fixar a data de referência. Se a norma era vigente à época: "nos termos da [norma], vigente à data do requerimento".

### 0.5 Checklist anti-alucinação — antes de entregar qualquer minuta

- [ ] Cada Tema/Súmula/REsp com número foi verificado OU está sinalizado como *[VERIFICAR]*
- [ ] Nenhuma ementa reconstituída de memória
- [ ] Carência e qualidade de segurado calculadas sobre CNIS conferido (não de memória)
- [ ] DII/DID/nexo ancorados em prova médica do caso
- [ ] Norma escolhida corresponde à data de referência (DER/óbito/DII)
- [ ] Valores e datas conferidos no documento de origem
- [ ] Todo item pendente sinalizado com *[VERIFICAR ANTES DE PROTOCOLAR]* e listado ao usuário

### 0.6 Protocolo de entrega com itens pendentes

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ITENS A VERIFICAR ANTES DO PROTOCOLO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[N] itens precisam ser verificados:
1. [Localização — Seção X] | Item: [o que verificar] | Tipo: [precedente/norma/dado/cálculo] | Risco se não verificado: [...]
AÇÃO RECOMENDADA: [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 0.7 Conduta em caso de dúvida

**Regra única:** sinalizar ou usar prosa genérica. Nunca resolver a dúvida inventando. O número fictício destrói a credibilidade da peça inteira quando descoberto — e em previdenciário, a PGF confere CNIS, datas e Temas.

---

## 1. WORKFLOW SEQUENCIAL — TRÊS FLUXOS

### Fluxo completo (padrão)
```
[1] INTAKE → [2] MAPA BRUTO → [3] DECISÃO ESTRATÉGICA → [4] ARQUITETURA → [5] REDAÇÃO → [6] REVISÃO
```
Usar quando: há tempo, informação adequada, risco médio ou alto.

### Fluxo abreviado (prazo apertado / informação parcial)
```
[1] INTAKE REDUZIDO → [2] MAPA SIMPLIFICADO → [3] REDAÇÃO COM RESSALVAS → [4] CHECKLIST FINAL
```
Condições: registrar *[FLUXO ABREVIADO]* + semáforo de suficiência + mapa mínimo (tese central + 2-3 pontos de maior risco) + ressalvas finais.

### Fluxo emergencial (prazo recursal hoje / decadência iminente)
```
[1] INTAKE MÍNIMO → [2] TESE CENTRAL + SILÊNCIO CRÍTICO → [3] REDAÇÃO DIRETA
```
Condições: registrar *[FLUXO EMERGENCIAL — sem mapa. Risco assumido. Revisão obrigatória antes do protocolo.]* + grau de confiança BAIXO automático + lista pós-entrega do que revisar.

**Acionamento:** o fluxo decorre de prazo + suficiência. Se não especificado, perguntar: *"Qual o prazo real e há prazo decadencial/recursal correndo?"* Nenhuma etapa é pulada sem registro explícito.

---

## 2. INTAKE — EXTRAÇÃO ESTRUTURADA

### 2.1 Perguntas de entrada (sempre fazer)

**Objetivo e finalidade:**
- Objetivo real (não o pedido formal): concessão, restabelecimento, conversão de espécie, revisão, só atrasados?
- Resultado mínimo aceitável; objetivos secundários (ex.: fixar DIB para maximizar atrasados).
- Horizonte: ganhar agora / construir prova para fase seguinte / posição para acordo.

**Ambiente decisório:**
- Fase: administrativa (INSS / CRPS — Junta de Recursos ou Câmara de Julgamento) ou judicial (JEF, vara federal, Turma Recursal, TNU, STJ)?
- Juízo/Turma e orientação predominante na matéria.
- Há precedente do próprio juízo/relator aplicável?

**Fatos:**
- Incontroversos (vínculos, datas, doença, óbito).
- Sensíveis ou exploráveis pelo INSS (perda de qualidade, ausência de carência, DII pré-filiação, vínculo glosável).
- Cronologia (filiação → contribuições → fato gerador → DER → indeferimento → DCB).

**Prova:**
- O que existe (CNIS, CTPS, PPP, LTCAT, laudos, prontuário, início de prova material).
- O que falta e pode ser obtido.
- Qual prova/fundamento do INSS é vulnerável (laudo administrativo lacônico, glosa sem motivação).

**Estratégia:**
- O que NÃO deve ser dito/ampliado/provocado nesta peça.
- Houve **prévio requerimento administrativo**? DER e fundamento exato do indeferimento? (Tema 350/STF)
- Risco tolerável; capacidade do segurado de aguardar.

### 2.2 Semáforo de suficiência informacional

| Status | Critério | Conduta |
|---|---|---|
| **SUFICIENTE** | Todos os elementos críticos disponíveis | Prosseguir |
| **PARCIAL** | Críticos presentes; complementares ausentes | Prosseguir com registro de lacunas e riscos |
| **INSUFICIENTE** | Crítico ausente que compromete o diagnóstico | Não avançar — solicitar primeiro |

```
SUFICIÊNCIA INFORMACIONAL: [SUFICIENTE / PARCIAL / INSUFICIENTE]
Pode avançar em: [...]
Falta: [...]
Risco de avançar sem isso: [...]
```

**Elementos críticos por área:**
- **INC (incapacidade):** CNIS + documentação médica contemporânea ao requerimento + laudo da perícia administrativa (ou judicial). Sem prova médica, a tese de DII é especulativa.
- **APO (aposentadoria):** CNIS completo + CTPS + PPP/LTCAT (se especial) + cálculo de tempo. Sem CNIS conferido, qualquer afirmação de tempo/carência é chute.
- **DEP (pensão):** certidão de óbito + prova de dependência/união + comprovação da qualidade de segurado do instituidor na data do óbito.
- **BPC:** laudo/perícia da deficiência (modelo biopsicossocial) + composição e renda do grupo familiar (CadÚnico). Não exige qualidade de segurado/carência.
- **REV (revisão):** carta de concessão + memória de cálculo da RMI + extrato dos salários-de-contribuição. Sem a memória, não se identifica o erro.
- **RPPS:** identificação do ente + norma local vigente + certidão de tempo + ato de aposentadoria (se já concedida).
- **ADM/JUD:** cópia integral do processo administrativo + comprovante de DER e da decisão impugnada com data de ciência (tempestividade/decadência).

### 2.3 Documentos prioritários

**Incapacidade:** processo administrativo completo, laudo da perícia do INSS, atestados/exames/prontuário contemporâneos, CNIS, CTPS.
**Aposentadoria:** CNIS, CTPS, PPP, LTCAT, carnês/GPS, prova de atividade rural (início de prova material), cálculo de tempo.
**Pensão:** certidão de óbito, prova do vínculo/dependência, CNIS do instituidor.
**Revisão:** carta de concessão, memória de cálculo, extrato CNIS dos salários-de-contribuição.

**Regra universal:** nunca presumir conteúdo de documento não recebido. Trabalhar só com o que foi enviado.

---

## 3. MAPA BRUTO — QUADRANTE PADRÃO

```
FAVORÁVEL (fático)               | DESFAVORÁVEL (fático)
─────────────────────────────────┼──────────────────────────────────
Fatos + prova + como usar        | Fatos + exposição + fragilidade + tratamento
FAVORÁVEL (jurídico)             | DESFAVORÁVEL (jurídico)
─────────────────────────────────┼──────────────────────────────────
Lei/EC → Jurisprudência → Doutrina | Como neutralizar/silenciar (com fundamento do INSS)
```

### 3.1 Decisão estratégica por ponto

| Decisão | Quando usar |
|---|---|
| **AMPLIFICAR** | Elemento favorável — realçar, aprofundar, documentar |
| **INSERIR** | Favorável omitido — incluir com prova |
| **NEUTRALIZAR** | Desfavorável com argumento disponível — rebater diretamente |
| **ENFRENTAR** | Desfavorável de alto risco — resposta frontal e completa |
| **MINIMIZAR** | Desfavorável de baixo valor sem argumento forte — tratar brevemente |
| **DESLOCAR** | Desfavorável sem saída direta — reconfigurar o enquadramento |
| **SILENCIAR** | Desfavorável sem argumento cujo silêncio não será lido como concordância |

### 3.2 Silêncio estratégico — campo obrigatório e categorizado

| Ponto | Categoria | Razão | Risco do silêncio | Decisão |
|---|---|---|---|---|

- **SILENCIAR** — não mencionar. Avaliar sempre se o INSS/juízo lerá o silêncio como admissão (ex.: silenciar sobre um vínculo frágil que não foi objeto de glosa).
- **DESLOCAR** — reconfigurar enquadramento (ex.: "perda de qualidade" → "manutenção pelo período de graça estendido por desemprego involuntário").
- **MINIMIZAR** — tratar brevemente; aprofundar criaria destaque desnecessário.
- **ENFRENTAR** — resposta frontal; silêncio seria concordância e há argumento sólido.

Silêncio é decisão consciente — nunca omissão.

---

## 4. AVALIAÇÃO DE RISCO

| Dimensão | Perguntas |
|---|---|
| **Jurídico** | A tese se sustenta? Há Tema/Súmula contrário? O ônus está do lado certo? A norma corresponde à data de referência? |
| **Financeiro** | Impacto de cada desfecho (atrasados, RMI, sucumbência)? Há cálculo alternativo (espécie/DIB menos arriscada)? |
| **Pessoal / assistencial** | O segurado depende do benefício para subsistência? Há urgência que justifique tutela? |
| **Processual** | Risco de extinção sem mérito (falta de prévio requerimento, decadência), sucumbência, custas |

Classificar cada risco **ALTO / MÉDIO / BAIXO** com justificativa.

---

## 5. ARQUITETURA DA PEÇA

Definir com o usuário antes de escrever: (1) estrutura de seções; (2) ordem dos argumentos (segue o indeferimento ponto a ponto ou agrupa por requisito: qualidade → carência → fato gerador → cálculo?); (3) seções próprias (cronologia, moldura fática, planilha de tempo/cálculo); (4) posição dos dados e evidências (no corpo — nunca em anexo); (5) extensão por seção (proporcional ao risco); (6) pedidos listados antes de redigir (concessão + DIB + atrasados + tutela + honorários — coerentes com o corpo).

---

## 6. PADRÃO DE REDAÇÃO

### 6.0 Profundidade — densidade não é brevidade

Densidade é ausência de palavra desperdiçada — cada frase acrescenta uma camada. Extensão é cobertura completa de cada argumento. Uma peça forte é **densa em cada linha e completa em cada tese**. Cortar o desenvolvimento de um argumento não o torna denso; torna-o amputado.

Regras de profundidade:
1. **Cada tese central é desenvolvida integralmente** na cadeia completa do §6.1.
2. **"Proporcional ao risco" tem piso, não só teto.** O ponto de alto risco (a perda de qualidade de segurado contestada, o nexo negado pela perícia) recebe *mais* desenvolvimento. MINIMIZAR só se aplica a ponto de baixo valor *e* baixo risco.
3. **A minuta entregue é texto redigido, pronto para protocolo.** Nunca tópicos, nunca "[desenvolver]".
4. **Teste de subdesenvolvimento (na revisão):** tese de alto risco resolvida em poucas linhas está subdesenvolvida — falta a interpretação do dispositivo, a *ratio* do precedente, a subsunção ao caso, a antecipação do contra-argumento ou o fechamento. Reabrir.

### 6.1 Estrutura interna de cada argumento

```
1. Lei/EC (dispositivo aplicável, na redação vigente à data de referência)
2. Jurisprudência (na hierarquia correta — Tema STF/STJ, Súmula TNU)
3. Doutrina (só quando acrescenta o que a jurisprudência não supre)
4. Dado concreto (CNIS, datas, planilha de tempo, cronologia médica — integrado ao corpo)
5. Conclusão (extração direta da cadeia, amarrada ao pedido)
```

Cada elo **se desenvolve** — não é uma frase por item:
- **Lei** — transcrever/parafrasear o dispositivo, fixar a interpretação e explicar por que se aplica (e por que a leitura do INSS não se sustenta).
- **Jurisprudência** — apresentar a tese fixada, expor a *ratio* e fazer a **subsunção explícita** ao caso (ou o *distinguishing* se for precedente contrário).
- **Dado concreto** — apresentar o dado (ex.: a tabela de vínculos do CNIS), contextualizá-lo e **extrair dele a consequência jurídica**.
- **Conclusão** — fechar o elo e amarrá-lo ao pedido.

Um argumento é uma **sequência de parágrafos**, não um parágrafo. Argumento de alto risco que coube em um parágrafo quase sempre perdeu um elo.

### 6.2 Integração de evidência

```
[Apresentar o fundamento do indeferimento / a conclusão da perícia]
[Inserir a tabela do CNIS / a cronologia médica / a planilha de tempo imediatamente]
[Extrair a conclusão jurídica do próprio dado]
```

A evidência é o argumento — não ilustração, não apêndice. A planilha de tempo de contribuição e a linha do tempo médica entram no corpo, no ponto em que destroem a tese do INSS.

### 6.3 Antecipação de contra-argumentos

Antecipar e desmontar os contra-argumentos típicos do INSS dentro da própria peça — antes que sejam levantados em contestação/recurso.

### 6.4 Tom por área

| Área | Tom |
|---|---|
| Incapacidade (JEF) | Técnico, objetivo, direto — juízo de alto volume; cronologia médica e crítica ao laudo no início |
| Aposentadoria / tempo / especial | Técnico, demonstrativo — a planilha de tempo e o PPP carregam o argumento |
| Pensão / dependentes | Técnico, sóbrio; sensibilidade na prova de dependência/união |
| BPC / LOAS | Técnico, com leitura social do conjunto probatório (deficiência biopsicossocial + miserabilidade) |
| Revisão / cálculo | Técnico-aritmético; a memória de cálculo é o eixo |
| Recurso administrativo (CRPS) | Objetivo, focado no enfrentamento do fundamento do indeferimento |
| RPPS | Técnico-constitucional; identificar a norma do ente é pré-condição |

---

## 7. CHECKLIST DE REVISÃO — TRANSVERSAL

### Camada 1 — Fática
- [ ] Há afirmação sem prova nos autos (vínculo, doença, dependência)?
- [ ] Há prova disponível não utilizada (documento do CNIS, atestado)?
- [ ] A cronologia (filiação/contribuições/fato gerador/DER) está correta?
- [ ] Algum fato foi amplificado além do que a prova sustenta?

### Camada 2 — Jurídica
- [ ] A tese central se sustenta sozinha?
- [ ] A norma corresponde à data de referência (tempus regit actum)?
- [ ] Nenhum Tema/Súmula com número permanece sem verificação?
- [ ] Há contradição interna entre seções?

### Camada 3 — Estratégica
- [ ] A peça convence este juízo/Turma específico?
- [ ] Algum requisito está superdimensionado frente ao risco real?
- [ ] O silêncio estratégico está mantido?

### Camada 4 — Protocolar
- [ ] Pedidos consistentes com os fundamentos (concessão + DIB + atrasados + tutela + honorários)
- [ ] Qualificação das partes e dados do benefício corretos (NB, DER, DCB)
- [ ] Nenhuma frase truncada ou pontuação dupla
- [ ] Citações literais entre aspas, atribuídas a documento verificado
- [ ] Nenhum vestígio de texto conversacional de IA no corpo da peça

---

## 8. GATE ANTI-PULO-DE-MAPA

Pedido direto de redação **não dispensa** os passos 3 (mapa) e 4-A (tensionamento) diante de qualquer um destes:

| Critério | Por que aciona |
|---|---|
| Alto impacto econômico | RMI alta, longo período de atrasados, benefício vitalício |
| Fundamento real do indeferimento não mapeado | Perícia? Carência? Qualidade? Falta de documento? — só aparece no mapa |
| Juízo/Turma adverso conhecido | Calibração de tom não é opcional |
| Horizonte decisório único | Tutela de urgência, decadência (art. 103 da Lei 8.213/91) iminente, recurso sem desdobramento |
| Laudo médico como peça central da decisão atacada | Exige matriz de vícios antes da redação (`pericia-medica-impugnacao.md`) |

Diante de qualquer um, confirmar o mapa antes de redigir. **Única exceção:** fluxo emergencial, com registro.

**Regra operacional:** "faça X" não dispensa o mapa quando a peça tem alto impacto. Respeitar a urgência é entregar peça forte, não peça rápida que depois precisa ser refeita.

---

## 9. CASOS HÍBRIDOS

**Regra 1 — Módulo primário pela arena decisória:** onde o caso será decidido (administrativo CRPS / JEF / vara federal / RPPS) define o módulo primário.
**Regra 2 — Módulo secundário** só quando muda algo na estratégia.
**Regra 3 — Conflito de orientação entre módulos:** prevalece (1) ambiente decisório; (2) objetivo real do segurado; (3) risco mais grave.

Combinações frequentes:

| Combinação | Primário | Secundário | Observação |
|---|---|---|---|
| Incapacidade + judicialização | INC | JUD | Laudo médico carrega `pericia-medica-impugnacao.md` obrigatoriamente |
| Aposentadoria especial + judicial | APO | JUD + Perícia | PPP/LTCAT como eixo; perícia técnica se houver |
| Pensão + qualidade de segurado controversa | DEP | RGPS | A manutenção da qualidade do instituidor é o pivô |
| Concessão + revisão (DIB/atrasados) | área da concessão | REV | Fixar DIB correta antes de calcular atrasados |
| BPC + incapacidade (segurado e deficiente) | conforme requisito atendido | — | BPC é subsidiário; não cumular com benefício do RGPS sobre o mesmo fato |
| RPPS + tese constitucional de transição | RPPS | REC | Identificar norma do ente é pré-condição |
| Qualquer área + recurso | REC | área principal | REC é transversal |
| Qualquer área + laudo médico | área principal | Perícia médica | Complementa, não substitui |
