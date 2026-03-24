### Pré-requisitos

### Para executar o projeto são necessários os seguintes componentes:

- Python 3.9 ou superior
- Ambiente virtual Python
- Dependências listadas em `requirements.txt`
- Playwright com o browser Chromium instalado
- Google Chrome ou Microsoft Edge para carregar a browser extension

##### Instalação

### Criar e ativar ambiente virtual:

python -m venv .venv
#source .venv/bin/activate

## Instalar dependências:

pip install -r requirements.txt
python -m playwright install chromium

#### Arranque do motor local

## O motor local é exposto através de uma API HTTP local. Para arrancar a API:

uvicorn engine.api.app:app --host 127.0.0.1 --port 8000 --reload

## Validação rápida do serviço:

curl http://127.0.0.1:8000/health

## Carregamento da browser extension

1. Abrir chrome://extensions/ ou edge://extensions/
2. Ativar Developer mode
3. Selecionar Load unpacked
4. Escolher a pasta extension/
5. Fluxo de utilização
6. Abrir uma página Web no browser
7. Abrir a browser extension
8. Confirmar o URL ativo apresentado no popup
9. Clicar em Capturar evidência
10. A extensão envia o pedido ao motor local
11. O motor local gera a pasta de execução e o ficheiro ZIP
12. O popup apresenta o caminho da execução e do pacote final


##### Execução direta via CLI

## A captura também pode ser executada diretamente por linha de comandos:

python -m engine.src.main capture https://example.com

## Exemplo com opções adicionais:

python -m engine.src.main capture https://example.com --output-dir output --timeout-ms 30000 --actor cli_user

##### Verificação de integridade

## Verificar uma pasta de execução:

python -m engine.src.main verify output/<nome_da_execucao>

## Verificar o ZIP final:

python -m engine.src.main verify output/<nome_da_execucao>/evidence_bundle.zip
Testes

## Executar a suite de testes:

python -m pytest -q

##### Estrutura principal do projeto

- extension/ browser extension
- engine/api/ API local
- engine/src/ motor de captura e preservação
- docs/ documentação de arquitetura e relatório
- tests/ testes automatizados
- output/ execuções geradas
