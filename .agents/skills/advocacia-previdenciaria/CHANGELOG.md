# CHANGELOG — advocacia-previdenciaria

Todas as alterações relevantes da skill são registradas aqui. Estado canônico de versão e maturidade fica em `references/_meta.md`.

---

## v1.0 — versão inicial

**Origem:** derivada metodologicamente de uma arquitetura de sistema jurídico de escritório (6 modos, Intenção Estratégica/Auftragstaktik, gates anti-pulo-de-mapa, padrão de redação por camadas, anti-alucinação). **Toda identidade do escritório de origem foi removida** — sem titular, OAB, CNPJ, sede, benchmarks de casos próprios, referências a SaaS ou a outras skills do autor original. A personalização passou a um template preenchível (`perfil-operador.md`).

**Escopo:** RGPS como eixo primário (segurado × INSS) + RPPS como módulo secundário. Reescopável.

### Adicionado

**Núcleo / orquestração**
- `SKILL.md` — orquestrador: 6 modos (TRIAGEM, DIAGNÓSTICO, ESTRATÉGIA, MINUTA, REVISÃO, MANUTENÇÃO) + camada EXECUTIVO; Intenção Estratégica com Restraints/Constraints; faixas de tolerância a risco; gates; Passo 0-4-A; hierarquias de autoridade por regime; regras globais anti-alucinação.
- `references/motor-comum.md` — motor metodológico universal: anti-alucinação, fluxos, intake, mapa/quadrante, risco, arquitetura, padrão de redação (densidade≠brevidade; estrutura interna Lei→Juris→Doutrina→Dado→Conclusão), checklist 4 camadas, gate, casos híbridos.
- `references/formato-saida.md` — grau de confiança obrigatório; pergunta TÉCNICO/EXECUTIVO; blocos de saída por modo (com datas-chave DER/DIB/DCB/DII/DID).
- `references/intencao-estrategica-por-modo.md` — Auftragstaktik por modo.

**Método de qualidade**
- `references/revisao-forense.md` — 6 camadas de revisão crítica.
- `references/pesquisa-jurisprudencial.md` — hierarquia de cortes; Gate de Enriquecimento; Devil's Advocate jurisprudencial; §4 casos-sentinela de volatilidade.
- `references/precedentes-distinguishing-overruling.md` — técnica de distinção/superação.
- `references/padroes-argumentativos.md` — 7 técnicas argumentativas genéricas.
- `references/seguranca-ingestao.md` — protocolo de ingestão de documentos.
- `references/sub-skills/` — `_schema.md`, `devils-advocate.md`, `tensionamento-adversario.md`, `juiz-externo.md`.

**Domínio probatório e perfis**
- `references/prova-e-documentos.md` — CNIS, CTPS, PPP/LTCAT, início de prova material, ônus, não-presunção.
- `references/pericia-medica-impugnacao.md` — impugnação substantiva de perícia médica (tripé DID/DII/DCB; tipologia de vícios; contradição interna; quesitos; seleção de vícios). **Módulo crítico.**
- `references/perfil-julgador.md` — calibragem por foro (INSS, CRPS, JEF, Turma Recursal, vara comum, TNU, STJ, STF, RPPS). Esqueleto + slot local.
- `references/perfil-operador.md` — **TEMPLATE** preenchível (substitui o antigo perfil de escritório). Skill opera em modo neutro enquanto não preenchido.

**Módulos de área**
- `rgps-fundamentos.md`, `incapacidade.md`, `aposentadorias.md`, `beneficios-dependentes.md`, `bpc-loas.md`, `revisoes-e-calculo.md`, `rpps.md`, `contencioso-administrativo-inss.md`, `judicializacao.md` (com camada de recursos).

**Controle**
- `references/_meta.md` — fonte única de estado e itens voláteis sob vigilância.
- `references/_licoes-aprendidas.md` — L-001, L-002, L-004 genericizadas + slots.

### Postura anti-alucinação (decisão estruturante)
- Específicos voláteis de lei (carências, números da EC 103, teto/SM, INs, prazos) entram como `[VERIFICAR]` em vez de afirmados.
- Três fatos voláteis datados e marcados: **revisão da vida toda** (tese cancelada pelo STF), **descontos associativos / ADPF 1236** (acordo estruturante em execução), **EC 103/teto** (parâmetros anuais). Situação de referência: mai/2026.

### Pendências assumidas (para evolução)
- Todos os módulos em maturidade ESQUELETO — validar contra casos reais e incorporar lições (L-005+).
- `perfil-operador.md` e slot local de `perfil-julgador.md` a preencher pelo operador.
