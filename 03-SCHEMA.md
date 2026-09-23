# Esquema de Metadados (Frontmatter YAML): Segundo Cérebro

Todas as notas de conhecimento, clientes, modelos e transcrições do Segundo Cérebro devem conter um cabeçalho YAML estruturado.
Isso permite que a inteligência artificial filtre, classifique e consulte notas instantaneamente sem precisar ler o corpo completo dos arquivos, economizando tokens.

---

## 1. Esquema para Ficha de Cliente / Caso (`10-clientes/`)

```yaml
---
tipo: caso
cliente: "Nome Completo do Cliente"
cpf_cnpj: "000.000.000-00"
processo: "0000000-00.0000.8.26.0000"
vara_comarca: "1ª Vara Cível de Tatuí"
area: civel # civel | familia | previdenciario | trabalhista
fase_atual: "Instrução e Provas"
advogada_responsavel: "Dra. Laura Oliveira"
estagiaria_designada: "Maria Carolina"
pasta_drive: "G:\\Meu Drive\\escritorio oliveira viana\\10-clientes\\Nome do Cliente"
status: ativo # ativo | suspenso | arquivado
atualizado_em: "AAAA-MM-DD"
---
```

---

## 2. Esquema para Peça Modelo / Tese (`20-modelos/` e `30-teses/`)

```yaml
---
tipo: modelo # modelo | tese
titulo: "Ação de Alimentos c/c Fixação de Guarda e Tutela Provisória"
area: familia # familia | civel | previdenciario
tribunal_alvo: TJSP
juizo_preferencial: "Vara de Família e Sucessões"
teses_chave:
  - "Binômio necessidade-possibilidade"
  - "Alimentos provisórios inaudita altera parte"
  - "Fixação de guarda unilateral com convivência assistida"
padrao_aprovado_por: "Dra. Laura Oliveira"
revisado_em: "AAAA-MM-DD"
arquivo_origem: "G:\\Meu Drive\\escritorio oliveira viana\\20-modelos\\inicial_alimentos_padrao.docx"
status: aprovado # aprovado | em_revisao
---
```

---

## 3. Esquema para Transcrições & Reuniões (`90-transcricoes/`)

```yaml
---
tipo: transcricao
assunto: "Reunião de Alinhamento e Governança Comercial"
data: "AAAA-MM-DD"
participantes:
  - "Leo Cauchioli"
  - "Dra. Iara Viana"
  - "Dra. Laura Oliveira"
frente: comercial # comercial | juridico | gestao
duracao_aproximada: "01:20:00"
status: processado # bruto | processado
---
```
