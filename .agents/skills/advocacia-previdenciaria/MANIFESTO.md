# advocacia-previdenciaria — Manifesto de Entrega

Skill autônoma de **advocacia previdenciária** (PT-BR), construída a partir da *dinâmica* de um sistema jurídico de escritório — método, arquitetura de modos, gates de qualidade e padrão de redação — **sem nenhuma identidade do escritório de origem**.

---

## O que esta skill é

Um sistema de raciocínio jurídico previdenciário operável por qualquer advogado. Cobre o ciclo completo: triagem → diagnóstico → estratégia → minuta → revisão crítica, com camada de sumário executivo. Eixo primário **RGPS** (segurado × INSS: incapacidade, aposentadorias, dependentes, BPC, revisões, contencioso administrativo e judicial) + módulo **RPPS** secundário.

## O que esta skill NÃO traz (por decisão)

Nenhum dado pessoal, timbre, OAB, CNPJ, sede, caso-benchmark, ou referência a sistemas/produtos do autor original. A identidade foi substituída por um **template preenchível**.

## Como o colega coloca a skill para funcionar

1. **Instalar** a pasta `advocacia-previdenciaria/` como skill.
2. **Preencher `references/perfil-operador.md`** — nome, OAB, foro, voz, repertório, atenções. Enquanto não preencher, a skill produz peça tecnicamente correta em **modo neutro** (sem voz autoral). Campo vazio é ignorado; não inventar dado.
3. (Opcional) **Preencher o slot local de `references/perfil-julgador.md`** com a experiência nos foros onde atua.
4. Usar normalmente: descrever o caso; a skill faz triagem, pede o que falta e segue o fluxo.

## Regra de ouro embutida (anti-alucinação)

A skill **não afirma número de lei, súmula, tema ou tese que não tenha sido conferido**. Específicos voláteis aparecem marcados `[VERIFICAR]` — para o operador confirmar na fonte oficial antes de levar à peça. Três pontos sensíveis já vêm datados e sinalizados:

- **Revisão da vida toda** — tese **cancelada** pelo STF; jamais apresentar como vigente.
- **Descontos associativos indevidos (ADPF 1236)** — acordo estruturante em execução; conferir a fase atual.
- **EC 103/2019 e teto do RGPS** — parâmetros mudam por ano; conferir sempre.

Situação de referência destes pontos: **maio/2026**. Reconferir periodicamente (`references/_meta.md` lista os itens sob vigilância).

## Escopo reescopável

A divisão RGPS-primário / RPPS-secundário é uma decisão de partida, não uma trava. Se o colega atua majoritariamente em RPPS, ou em nicho (só incapacidade, só rural, só BPC), os módulos de área e o `perfil-operador.md` permitem reorientar o peso sem refazer o núcleo.

## Integridade

Entrega como pacote completo: `SKILL.md` + todos os módulos de `references/` (incl. `sub-skills/`) + `CHANGELOG.md` + este manifesto. Estado canônico de versão/maturidade em `references/_meta.md`.

---

**v1.0** — todos os módulos em maturidade ESQUELETO (método estável; repertório a calibrar em uso real). Evolução prevista: validar contra casos concretos e incorporar lições via protocolo em `references/_licoes-aprendidas.md`.
