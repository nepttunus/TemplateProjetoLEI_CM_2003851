# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Scaffold inicial do MVP em Python para captura de evidência web com preservação de integridade.

## O que este MVP já faz

- recebe uma URL por linha de comandos
- abre a página com Playwright
- guarda uma screenshot em PNG
- guarda o HTML final da página
- recolhe metadados básicos da captura
- calcula hashes SHA-256 dos artefactos
- gera um `manifest.json`
- cria um `ZIP` com os artefactos e o manifesto
- verifica a integridade do conjunto
- inclui teste negativo simples de integridade

## Estrutura

```text
osint_evidence_mvp/
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
```

## Preparação do ambiente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Exemplos de uso

### 1) Capturar uma página

```bash
python src/main.py capture https://example.org
```

### 2) Capturar com pasta de saída definida

```bash
python src/main.py capture https://example.org --output-dir output
```

### 3) Capturar com browser visível

```bash
python src/main.py capture https://example.org --headed
```

### 4) Verificar um pacote ZIP gerado

```bash
python src/main.py verify output/example_org_20260320T210000Z/evidence_bundle.zip
```

### 5) Verificar uma pasta extraída

```bash
python src/main.py verify output/example_org_20260320T210000Z
```


## Fluxo do MVP

1. `capture.py` abre a URL, espera pelo carregamento da página e grava os artefactos.
2. `hashing.py` calcula o SHA-256 de cada ficheiro relevante.
3. `manifest.py` gera um manifesto JSON com metadados e hashes.
4. `package.py` cria um ZIP final do conjunto de evidência.
5. `verify.py` valida se todos os ficheiros listados no manifesto continuam íntegros.

## Critério de aceitação observável

Uma execução de captura é considerada bem-sucedida quando:

- existe uma pasta de execução com `artifacts/`, `manifest.json` e `evidence_bundle.zip`
- o `manifest.json` contém hashes SHA-256 dos artefactos gravados
- a verificação devolve sucesso para um conjunto não alterado
- a verificação devolve falha se um artefacto for alterado depois da captura

## Limitações atuais do MVP

- apenas usa Chromium
- não recolhe ainda HAR, console logs ou network dump detalhado
- não faz normalização avançada de URLs
- não implementa ainda cadeia de custódia formal nem assinatura digital

## Próximos incrementos naturais

- exportação HAR e logs de consola
- captura opcional em PDF
- recolha de headers/resposta base
- assinatura do manifesto
- geração de relatório resumido em JSON/Markdown
- testes automáticos com páginas controladas
