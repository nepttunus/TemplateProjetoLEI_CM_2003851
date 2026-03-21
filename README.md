# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Scaffold evolutivo do MVP em Python para captura de evidência web com preservação de integridade.

## O que este MVP já faz

- recebe uma URL por linha de comandos
- abre a página com Playwright
- guarda uma screenshot em PNG
- guarda o HTML final da página
- guarda metadados básicos da captura
- guarda metadados HTTP da resposta principal
- guarda logs de consola da página
- guarda um ficheiro HAR de rede
- guarda um trace ZIP do browser
- calcula hashes SHA-256 dos artefactos
- gera um `manifest.json`
- cria um `ZIP` com os artefactos e o manifesto
- verifica a integridade do conjunto
- inclui testes automáticos para hashing, verificação, artefactos HTTP/consola e HAR/trace

## Estrutura

```text
TemplateProjetoLEI_CM_2003851/
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── capture.py
│   ├── hashing.py
│   ├── manifest.py
│   ├── package.py
│   └── verify.py
├── tests/
├── output/
├── requirements.txt
└── README.md
