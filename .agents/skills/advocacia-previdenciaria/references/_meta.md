# _meta — Fonte Única de Estado

*Arquivo de controle. Carregar em MANUTENÇÃO. Consultar no início de qualquer sessão de evolução da skill.*

---

## Versão

**v1.0** — versão inicial. Skill autônoma de advocacia previdenciária, derivada metodologicamente de uma arquitetura de sistema jurídico de escritório, sem identidade do escritório de origem.

## Princípio de estado

Este arquivo é a **única fonte de verdade** sobre versão e maturidade dos módulos. Qualquer divergência entre o que outro arquivo afirma e o que está aqui resolve-se a favor deste arquivo. Atualizar aqui ao fechar sessão de manutenção.

## Maturidade dos módulos

Escala: `ESQUELETO` (estrutura + método, sem repertório calibrado em caso real) → `EM USO` (validado contra ao menos um caso real) → `MADURO` (validado contra múltiplos casos, com lições incorporadas).

| Módulo | Maturidade | Observação |
|---|---|---|
| motor-comum.md | ESQUELETO | núcleo metodológico estável |
| SKILL.md (orquestração) | ESQUELETO | 6 modos + gates |
| rgps-fundamentos.md | ESQUELETO | — |
| incapacidade.md | ESQUELETO | — |
| aposentadorias.md | ESQUELETO | regras de transição EC103 marcadas [VERIFICAR] |
| beneficios-dependentes.md | ESQUELETO | — |
| bpc-loas.md | ESQUELETO | — |
| revisoes-e-calculo.md | ESQUELETO | revisão da vida toda marcada como CANCELADA; ADPF 1236 datada |
| rpps.md | ESQUELETO | depende da norma de cada ente — sempre [VERIFICAR] |
| contencioso-administrativo-inss.md | ESQUELETO | — |
| judicializacao.md | ESQUELETO | inclui camada de recursos |
| pericia-medica-impugnacao.md | ESQUELETO | metodologia substantiva — crítico |
| prova-e-documentos.md | ESQUELETO | — |
| perfil-julgador.md | ESQUELETO | preencher com experiência local |
| perfil-operador.md | TEMPLATE | preencher antes do primeiro uso autoral |

## Regra de não-acoplamento

A skill não tem dependência de versão com nenhum sistema externo, SaaS, ou outra skill. Evolui isoladamente.

## Itens voláteis sob vigilância (revisar a cada uso)

Estes pontos mudam por fato externo, não por decisão do operador. Sempre reconfirmar via fonte oficial / web antes de afirmar em peça:

1. **Teto do RGPS e salário mínimo do ano** — mudam anualmente.
2. **Revisão da vida toda** — tese cancelada pelo STF; disputa residual sobre modulação ainda em curso. Ver `revisoes-e-calculo.md` e `pesquisa-jurisprudencial.md` §4.
3. **Descontos associativos indevidos (ADPF 1236)** — acordo estruturante em execução; prazos e fases mudam. Ver `revisoes-e-calculo.md`.
4. **Regras de transição da EC 103/2019** — estáveis em texto, mas pontos de cálculo (pedágio, idade progressiva) exigem conferência por ano.
5. **Instruções Normativas do INSS** — substituídas com frequência; confirmar a IN vigente na data do ato.
