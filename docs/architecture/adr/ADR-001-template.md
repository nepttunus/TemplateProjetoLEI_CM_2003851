# ADR 0001 - Escolha da stack tecnológica principal

## Estado
Aceite

## Contexto
O projeto pretende implementar uma plataforma modular para captura e preservação de evidência digital OSINT. O núcleo funcional do MVP exige captura de páginas web, geração de screenshots, manipulação de ficheiros, cálculo de hashes, criação de ficheiros ZIP e execução de testes automatizados.

## Decisão
A stack principal do projeto será composta por Python, Playwright, SQLite, JSON e SHA-256.

## Justificação
Python apresenta boa legibilidade, rapidez de desenvolvimento e um ecossistema adequado ao problema em causa. Playwright foi escolhido por suportar páginas modernas com conteúdo dinâmico. SQLite é suficiente para a persistência local prevista no MVP. JSON é adequado para o manifesto de evidência e SHA-256 é apropriado para verificação de integridade.

## Alternativas consideradas
- Node.js + Playwright
- PowerShell
- Selenium

## Consequências
A implementação será centrada numa aplicação Python modular, com núcleo CLI e possibilidade de evolução futura.
