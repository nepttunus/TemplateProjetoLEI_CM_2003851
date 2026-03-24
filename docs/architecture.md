# Arquitetura da Solução

## Visão Geral
A solução proposta é composta por uma browser extension, que funciona como ponto de entrada para o utilizador, e por um motor local responsável pela captura controlada, preservação, hashing e empacotamento da evidência digital.

## Componentes
- Browser Extension
- Local API / Bridge
- Motor Local de Captura
- Camada de Preservação
- Pacote de Evidência

## Fluxo de Execução
1. O utilizador abre a página alvo no browser.
2. A extensão obtém o URL ativo.
3. O utilizador inicia a captura através da extensão.
4. A extensão envia um pedido ao motor local.
5. O motor local executa a captura da página.
6. O motor local gera screenshot, HTML e metadados.
7. O motor local calcula hashes e gera o manifest JSON.
8. O motor local cria o pacote ZIP final.
9. A extensão recebe a confirmação da operação.

## Justificação Arquitetural
A separação entre interface e motor técnico permite melhorar a usabilidade, modularidade e coerência do produto final. A extensão simplifica a interação com o utilizador, enquanto o motor local concentra as funções de captura e preservação, facilitando a validação técnica e a defesa académica da solução.
