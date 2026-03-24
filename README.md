# Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

Este projeto implementa uma plataforma modular de captura e preservação de evidência digital para contexto OSINT.

A solução evoluiu de uma prova de conceito inicial orientada a linha de comandos para uma arquitetura composta por uma browser extension, responsável pela interação com o utilizador, e por um motor local dedicado à captura controlada, preservação, hashing e empacotamento da evidência digital.

## Objetivo
Permitir a recolha estruturada de evidência digital a partir do browser, delegando a captura, preservação, hashing e empacotamento para um motor local.

## Utilizador-alvo
Analistas, investigadores e utilizadores técnicos em contexto OSINT/DFIR.

## Resultado esperado
Gerar um pacote de evidência com screenshot, HTML, metadados, hashes e manifest JSON.

## Estrutura
- `extension/` interface do utilizador no browser
- `engine/` motor local de captura e preservação
- `docs/` documentação técnica e de projeto
- `tests/` testes automatizados
- `samples/` amostras e exemplos

## Fluxo do MVP
1. O utilizador abre uma página Web no browser.
2. A browser extension obtém o URL ativo.
3. O utilizador inicia a captura através da extensão.
4. A extensão envia o pedido ao motor local via API HTTP.
5. O motor local executa a captura com Playwright.
6. São gerados artefactos, manifest, assinatura, cadeia de custódia e pacote ZIP.
7. O caminho da execução e do ZIP é devolvido à extensão.
8. A integridade pode ser verificada posteriormente.
