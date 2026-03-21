# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Scaffold evolutivo do MVP em Python para captura de evidência web com preservação de integridade.

## O que este MVP já faz

- recebe uma URL por linha de comandos
- abre a página com Playwright
- guarda uma screenshot em PNG
- guarda o HTML final da página
- guarda um PDF da página capturada
- guarda metadados básicos da captura
- guarda metadados HTTP da resposta principal
- guarda logs de consola da página
- guarda um ficheiro HAR de rede
- guarda um trace ZIP do browser
- calcula hashes SHA-256 dos artefactos
- gera um `manifest.json`
- cria um `ZIP` com os artefactos e o manifesto
- verifica a integridade do conjunto
- inclui testes automáticos para hashing, verificação, artefactos HTTP/consola, HAR/trace e PDF

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

## Preparação do ambiente

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium


## Exemplos de uso

Capturar uma página
python src/main.py capture https://example.org

Capturar com pasta de saída definida
python src/main.py capture https://example.org --output-dir output

Capturar com browser visível
python src/main.py capture https://example.org --headed

Verificar um pacote ZIP gerado
python src/main.py verify output/example.org_20260321T001321Z/evidence_bundle.zip

Verificar uma pasta extraída
python src/main.py verify output/example.org_20260321T001321Z

## Fluxo do MVP

capture.py abre a URL, espera pelo carregamento da página e grava os artefactos.
hashing.py calcula o SHA-256 de cada ficheiro relevante.
manifest.py gera um manifesto JSON com metadados de captura e de cada artefacto.
package.py cria um ZIP final do conjunto de evidência.
verify.py valida se todos os ficheiros listados no manifesto continuam íntegros.
Artefactos atualmente gerados
artifacts/screenshot.png
artifacts/page.html
artifacts/page.pdf
artifacts/capture_metadata.json
artifacts/http_metadata.json
artifacts/console_logs.json
artifacts/network.har
artifacts/trace.zip
manifest.json
evidence_bundle.zip


## Estrutura do manifesto

O manifest.json inclui agora:
versão de schema
data/hora de geração
diretório lógico da execução
metadados da captura
resumo com número de ficheiros e tamanho total
lista de ficheiros com:
caminho relativo
SHA-256
tamanho em bytes
timestamp de modificação
tipo lógico de artefacto
media type
nome do ficheiro


## Critério de aceitação observável

Uma execução de captura é considerada bem-sucedida quando:
existe uma pasta de execução com artifacts/, manifest.json e evidence_bundle.zip
o manifest.json contém hashes SHA-256 e metadados dos artefactos gravados
a verificação devolve sucesso para um conjunto não alterado
a verificação devolve falha se um artefacto for alterado depois da captura


## Limitações atuais do MVP
apenas usa Chromium
ainda não faz assinatura digital do manifesto
ainda não implementa cadeia de custódia formal
ainda não faz normalização avançada de URLs

##Próximos incrementos naturais
assinatura do manifesto
cadeia de custódia mínima
recolha adicional de headers e eventos relevantes
geração de relatório resumido em JSON/Markdown
testes automáticos adicionais para cenários de erro
