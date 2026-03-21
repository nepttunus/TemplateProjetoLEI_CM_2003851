# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Este repositório contém a versão final do MVP académico do projeto Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT. A solução foi implementada em Python e permite capturar uma URL, recolher artefactos relevantes, gerar um manifesto com hashes, assinar digitalmente esse manifesto, registar uma cadeia de custódia mínima, produzir relatórios por execução e verificar posteriormente a integridade e a autenticidade do conjunto.

A evolução do trabalho foi feita por incrementos sucessivos até à versão estabilizada do MVP. O estado validado do projeto encontra-se refletido na tag `v1.0`.

## Estado atual do projeto

O MVP encontra-se concluído e validado em ambiente local e em ambiente limpo. A validação final incluiu clonagem do repositório, criação de ambiente virtual, instalação das dependências, instalação do Chromium do Playwright, execução da suite de testes automáticos, captura de uma URL de referência e verificação do pacote final produzido.

A suite de testes inclui atualmente 14 testes automáticos com sucesso.

## Funcionalidades implementadas

O sistema permite

capturar uma página web a partir de uma URL

gerar screenshot em PNG

guardar o HTML final da página

exportar a página para PDF

recolher metadados básicos da captura

recolher metadados HTTP da resposta principal

recolher logs de consola

gerar um ficheiro HAR de rede

gerar um trace ZIP do browser

calcular hashes SHA 256 dos ficheiros relevantes

gerar um `manifest.json`

assinar o manifesto em `manifest.sig`

gerar uma chave pública por execução em `keys/public_key.pem`

gerar um `chain_of_custody.json` com eventos mínimos da execução

aceitar um ator lógico com `--actor`

gerar `report.json` e `report.md` com resumo da execução

criar um `evidence_bundle.zip`

verificar integridade e autenticidade do conjunto



## Estrutura do projeto

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
├── docs/
├── output/
├── requirements.txt
└── README.md



## Preparação do ambiente

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium


## Exemplos de utilização

# Captura simples
python -m src.main capture https://example.org
# Captura com ator lógico associado
python -m src.main capture https://example.org --actor "Carlos"

# Captura com browser visível
python -m src.main capture https://example.org --headed

# Verificação de uma pasta de execução
python -m src.main verify output/example.org_20260321T211845Z

# Verificação de um pacote ZIP
python -m src.main verify output/example.org_20260321T211845Z/evidence_bundle.zip


### Fluxo principal do sistema

O fluxo de captura segue uma sequência modular. Primeiro a página é aberta e os artefactos principais são gerados. Depois é produzido o registo de cadeia de custódia. Em seguida é criado o manifesto com hashes e metadados. O manifesto é assinado digitalmente. São também produzidos relatórios resumidos da execução. Por fim, todo o conjunto é empacotado em ZIP e pode ser posteriormente validado pelo módulo de verificação.


## Artefactos gerados por execução

# Cada execução pode produzir os seguintes elementos

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

keys/public_key.pem

report.json

report.md

evidence_bundle.zip



## Assinatura do manifesto

O projeto usa Ed25519 para assinatura digital do manifesto. Esta escolha foi adotada por ser simples, moderna, eficiente e adequada ao contexto do projeto. A assinatura é gerada para o ficheiro manifest.json e a chave pública é guardada na própria pasta de execução. Durante a verificação, se a assinatura existir, o sistema valida também a autenticidade do manifesto.

## Cadeia de custódia mínima

Cada execução produz um ficheiro chain_of_custody.json com eventos mínimos da recolha. Esses eventos incluem identificação temporal, ação realizada, ator lógico associado, alvo e detalhes relevantes. Entre os eventos atualmente registados encontram-se capture_started, capture_completed, keypair_generated, manifest_created, report_generated, manifest_signed e package_created.

## Relatórios por execução

# O projeto gera dois relatórios por execução.

report.json contém um resumo estruturado em formato JSON

report.md contém um resumo legível em Markdown

Estes relatórios registam a identificação da execução, a URL original, a URL final, o título da página, o estado HTTP e a lista de artefactos gerados.

Validação do projeto

A versão final do MVP foi validada em ambiente limpo. O repositório foi clonado para uma pasta nova, foi criado um ambiente virtual Python, instalaram-se as dependências previstas, foi instalado o browser Chromium do Playwright, executou-se a suite de testes e realizou-se uma captura integral da página de referência https://example.org com o ator lógico Carlos.

A suite automatizada terminou com sucesso, totalizando 14 testes passados.

Foi também validado o pacote ZIP final gerado, tendo a verificação devolvido sucesso com 12 ficheiros verificados e sem erros.

Adicionalmente foi realizado um teste negativo manual. Para esse efeito foi criada uma cópia de uma execução válida e alterado o ficheiro artifacts/page.html. Após essa modificação, a verificação devolveu erro e identificou explicitamente a mensagem Hash inválido: artifacts/page.html.

Foi ainda efetuada uma validação simples de desempenho através de três execuções consecutivas sobre a página https://example.org. Os tempos totais observados foram 2,499 segundos na primeira execução, 1,684 segundos na segunda e 1,302 segundos na terceira. Estes valores revelaram comportamento estável e adequado ao objetivo académico do projeto.



### Testes implementados

A suite cobre, entre outros, os seguintes cenários

captura de artefactos

geração de manifesto

assinatura e verificação do manifesto

cadeia de custódia

relatórios por execução

exportação PDF

recolha de console logs e metadados HTTP

HAR e trace

teste negativo de adulteração de ZIP

eventos de custódia com ator lógico



## Limitações atuais

O projeto utiliza apenas Chromium

a gestão de chaves é local e simplificada

a cadeia de custódia é mínima e não cobre workflows multiutilizador completos

não existe rotação formal de chaves

não foi realizada uma campanha formal de carga ou escalabilidade


## Repositório

Código fonte, histórico de desenvolvimento, versões e documentação encontram-se disponíveis em

https://github.com/nepttunus/TemplateProjetoLEI_CM_2003851



## Versão de referência

A versão de referência do MVP validado corresponde à tag

v1.0



### Próximos desenvolvimentos possíveis  ### 

Como evolução futura, o projeto poderá incluir uma cadeia de custódia mais rica, proteção reforçada da chave privada, rotação de chaves, relatórios mais detalhados e validações adicionais para cenários mais exigentes.
