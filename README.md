# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

**Projeto Final de Licenciatura em Engenharia Informática**  
**Estudante:** Carlos Marques (2003851)  
**Orientador:** Pedro Duarte Pestana

## Estado atual
O projeto encontra-se na fase inicial de definição detalhada do âmbito, do MVP e da arquitetura base. O repositório já está estruturado de acordo com o guia da unidade curricular e será atualizado ao longo do semestre.

## Resumo
Este projeto pretende desenvolver uma plataforma modular para captura e preservação de evidência digital proveniente de fontes OSINT. A solução deverá permitir recolher artefactos como HTML e screenshots, associar-lhes metadados, calcular hashes SHA-256 e gerar um pacote final verificável que suporte integridade e rastreabilidade.

O foco está na construção de um MVP simples, mas tecnicamente sólido, que permita demonstrar um fluxo completo de preservação de evidência em ambiente de laboratório.

## MVP previsto
- criação de casos
- captura de URL com geração de HTML e screenshot
- registo de metadados mínimos
- geração de `manifest.json`
- cálculo de hashes SHA-256
- exportação de pacote ZIP
- verificação de integridade do pacote

## Estrutura do repositório
- `docs/scope/` contém proposta, requisitos, changelog e riscos
- `docs/architecture/` contém diagramas e ADRs
- `docs/report/` contém material de apoio ao relatório
- `src/` irá conter o código-fonte do projeto

## Stack prevista
- Python
- Playwright
- SQLite
- JSON
- SHA-256
- pytest
