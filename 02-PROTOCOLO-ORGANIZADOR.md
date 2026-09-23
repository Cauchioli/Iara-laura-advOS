# Protocolo Organizador de Acervo: Método T.O.G.A / Vértice OS
## Aplicação: Google Drive (Pasta "Escritório Oliveira Viana")

Este protocolo estabelece o procedimento padronizado para inventariar, classificar e organizar o acervo digital do escritório Iara & Laura Advocacia sem que um único arquivo seja perdido ou corrompido.

---

## 1. As Leis Inegociáveis do Organizador

1. Proibição Absoluta de Apagar:
   - Nenhum arquivo ou pasta pode ser excluído diretamente. Arquivos candidatos a descarte são movidos para uma pasta de quarentena datada (`_lixo-AAAA-MM-DD\`). Somente as sócias têm autorização para esvaziar essa pasta.
2. A Lei da Caixa Lacrada:
   - Pastas de processos judiciais originárias de tribunais (PJe, e-SAJ, Projudi, eproc) ou identificadas por número CNJ (`0000000-00.0000.0.00.0000`) são caixas lacradas. Elas podem ser movidas inteiras para o diretório do cliente, mas seu conteúdo interno é intocável (não renomear nem alterar).
3. Documentos Fiscais e Societários são Intocáveis:
   - CNDs, notas fiscais, DARFs, guias, comprovantes e livros contábeis jamais são movidos para quarentena.
4. Parada Obrigatória para Aprovação:
   - A inteligência artificial só move qualquer arquivo após as sócias responderem expressamente "APROVO" ao plano proposto. Antes dessa resposta, toda operação é exclusivamente de leitura.
5. Registro em Tempo Real:
   - Toda e qualquer movimentação é registrada linha por linha no momento em que ocorre no arquivo `00-LOG-movimentacoes.md` (no formato `| origem | destino | data |`).

---

## 2. O Fluxo de Execução em Três Fases

### Fase 1: Inventário com Lacre (Somente Leitura)
1. Varredura completa da pasta raiz do Drive do escritório.
2. Geração do relatório `00-INVENTARIO.md` contendo:
   - Total exato de arquivos e pastas (o número do "Lacre").
   - Contagem por extensão (PDF, DOCX, XLSX, imagens).
   - Identificação das pastas com maior volume e detecção de duplicatas nominais.
   - Lista separada de todas as pastas de processos judiciais lacradas.

### Fase 2: Proposta de Organização (Parada Obrigatória)
1. Elaboração do arquivo `00-PLANO.md` apresentando a árvore padronizada do escritório:
   ```text
   escritorio oliveira viana/
   ├── 00-TRIAGEM/                  # Documentos recém-chegados não classificados
   ├── 10-clientes/                 # Pastas nominais de clientes [Nome do Cliente]
   │   └── [Processos, Contratos, Documentos Pessoais]
   ├── 20-modelos/                  # Modelos oficiais de petições do escritório
   ├── 30-administrativo/           # Modelos de contratos, procurações e POPs
   ├── 40-financeiro/               # Pasta restrita e blindada das sócias
   ├── 50-estudos-e-referencias/    # Doutrina, jurisprudência e materiais de apoio
   └── 80-arquivo-morto/            # Casos encerrados e arquivados
   ```
2. Apresentação da tabela DE para PARA com todas as movimentações sugeridas.
3. Solicitação de validação expressa: *"Leia o plano proposto. Digite APROVO para executar ou indique os ajustes desejados."*

### Fase 3: Execução Assistida e Verificação de Lacre
1. Movimentação gradual dos arquivos com registro simultâneo no log.
2. Tratamento de conflito de nomes (adição do sufixo `-v2` para evitar sobrescrita).
3. Conferência final: checagem se o número total de arquivos corresponde exatamente ao Lacre inicial da Fase 1.
