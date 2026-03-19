# Arquitectura

Esta pasta contém os artefactos de arquitectura do projecto.

## Ficheiros obrigatórios

| Ficheiro | Descrição | Quando |
|---------|-----------|--------|
| `c4-context.png` | C4 Nível 1 — sistema, utilizadores, sistemas externos | Até à Entrega 1 |
| `c4-containers.png` | C4 Nível 2 — contentores principais e tecnologias | Até à Entrega 1 |
| `data-model.png` | Modelo de dados (ER, schema, ou equivalente) | Até à Entrega 1 |
| `adr/` | Decisões de arquitectura | Durante todo o semestre |

## Notas sobre o modelo de dados

- **Base de dados relacional** (PostgreSQL, SQLite, MySQL): usar diagrama Entidade-Relação (ER)
- **Base de dados não-relacional** (MongoDB, Firebase, DynamoDB): usar schema diagram ou modelo de documentos
- **Sem base de dados persistente**: documentar a estrutura de dados em memória ou ficheiro

## Ferramentas sugeridas para os diagramas

- **C4:** [Structurizr](https://structurizr.com) (gratuito para uso individual) ou [draw.io](https://draw.io) com shapes C4
- **ER / modelo de dados:** [dbdiagram.io](https://dbdiagram.io) (gratuito) ou draw.io
- **Alternativa universal:** draw.io exporta PNG e é gratuito para tudo

## Referência C4

Documentação oficial: [c4model.com](https://c4model.com)  
Os níveis 1 e 2 são suficientes para a maioria dos projectos de licenciatura.
