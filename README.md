# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Scaffold evolutivo do MVP em Python para captura de evidência web com preservação de integridade, assinatura do manifesto, verificação de autenticidade, cadeia de custódia mínima e relatórios resumidos por execução.

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
- assina o manifesto em `manifest.sig`
- gera um par de chaves Ed25519 por execução e guarda a chave pública dentro da pasta da execução, em `keys/public_key.pem`
- gera um ficheiro `chain_of_custody.json` com eventos mínimos da cadeia de custódia
- aceita um ator lógico com `--actor` para registo da captura
- gera `report.json` e `report.md` com resumo da execução
- cria um `ZIP` com os artefactos, manifesto, assinatura, chave pública, registo de custódia e relatórios
- verifica a integridade do conjunto
- verifica a assinatura do manifesto quando existir
- inclui testes automáticos para hashing, verificação, artefactos HTTP/consola, HAR/trace, PDF, adulteração negativa de ZIP, assinatura do manifesto, cadeia de custódia, relatórios e eventos com ator

## Estrutura

```text
TemplateProjetoLEI_CM_2003851/
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── capture.py
│   ├── custody.py
│   ├── hashing.py
│   ├── manifest.py
│   ├── package.py
│   ├── reporting.py
│   ├── signature.py
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


##### Exemplos de uso


## Capturar uma página
python -m src.main capture https://example.org
## Capturar com pasta de saída definida
python -m src.main capture https://example.org --output-dir output
## Capturar com browser visível
python -m src.main capture https://example.org --headed
## Capturar indicando o ator lógico
python -m src.main capture https://example.org --actor "Carlos"
## Verificar um pacote ZIP gerado
python -m src.main verify output/example.org_20260321T001321Z/evidence_bundle.zip
## Verificar uma pasta extraída
python -m src.main verify output/example.org_20260321T001321Z


## Fluxo do MVP

capture.py abre a URL, espera pelo carregamento da página e grava os artefactos.
hashing.py calcula o SHA-256 de cada ficheiro relevante.
custody.py gera um registo mínimo de cadeia de custódia da execução.
manifest.py gera um manifesto JSON com metadados de captura e de cada artefacto.
signature.py garante a existência do par de chaves, assina o manifesto e disponibiliza validação de assinatura.
reporting.py gera relatórios resumidos em JSON e Markdown.
package.py cria um ZIP final do conjunto de evidência.
verify.py valida se todos os ficheiros listados no manifesto continuam íntegros e, quando existir assinatura, valida também a autenticidade do manifesto.


## Artefactos atualmente gerados
artifacts/screenshot.png
artifacts/page.html
artifacts/page.pdf
artifacts/capture_metadata.json
artifacts/http_metadata.json
artifacts/console_logs.json
artifacts/network.har
artifacts/trace.zip
chain_of_custody.json
manifest.json
manifest.sig
keys/public_key.pem dentro da pasta da execução
report.json
report.md
evidence_bundle.zip


### Estrutura do manifesto

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


## Assinatura do manifesto

O projeto usa assinatura digital Ed25519 para reforçar a autenticidade do manifest.json.

Em cada captura:

o manifesto é assinado e guardado em manifest.sig
a chave pública é guardada dentro da pasta da execução, em keys/public_key.pem
a chave privada é usada localmente para assinar e não deve ser distribuída no pacote final de evidência

Durante a verificação:

se existir manifest.sig, a verificação valida a assinatura do manifesto
se a assinatura não corresponder ao conteúdo atual do manifesto, a verificação falha
se a chave pública estiver em falta, a verificação também falha
Cadeia de custódia mínima

O projeto gera um ficheiro chain_of_custody.json por execução para registar eventos essenciais da recolha de evidência.

Cada evento inclui:

event_id
timestamp
action
actor
target
details

Exemplos de ações atualmente registadas:

capture_started
capture_completed
keypair_generated
manifest_created
report_generated
manifest_signed
package_created
Relatórios por execução

O projeto gera dois relatórios resumidos por execução:

report.json com resumo estruturado
report.md com resumo legível em Markdown

O resumo inclui:

identificação da execução
URL original e URL final
título da página
status HTTP
timestamps de início e fim
lista de artefactos incluídos
referência ao manifesto e à assinatura
Critério de aceitação observável

Uma execução de captura é considerada bem-sucedida quando:

existe uma pasta de execução com artifacts/, chain_of_custody.json, manifest.json, manifest.sig, keys/public_key.pem, report.json, report.md e evidence_bundle.zip
o manifest.json contém hashes SHA-256 e metadados dos artefactos gravados
existe um chain_of_custody.json com eventos mínimos da execução
a assinatura do manifesto é validada com sucesso quando o conteúdo não foi alterado
a verificação devolve sucesso para um conjunto não alterado
a verificação devolve falha se um artefacto for alterado depois da captura
a verificação devolve falha se o manifesto assinado for alterado

## Limitações atuais do MVP
apenas usa Chromium
a gestão de chaves ainda é local e simplificada
a cadeia de custódia ainda é mínima e não cobre workflows multiutilizador completos
ainda não faz normalização avançada de URLs
ainda não implementa rotação, proteção forte ou armazenamento seguro da chave privada

## Próximos incrementos naturais
cadeia de custódia com múltiplos atores e eventos adicionais
proteção segura da chave privada
rotação e gestão de chaves
recolha adicional de headers e eventos relevantes
relatórios mais detalhados com resumo técnico e executivo
testes automáticos adicionais para cenários de erro
