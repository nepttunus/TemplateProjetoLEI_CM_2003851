# Arquitetura da Solução

## Visão Geral
A solução implementada segue uma arquitetura modular composta por dois blocos principais: uma browser extension, responsável pela interação com o utilizador no contexto real de navegação, e um motor local de captura e preservação, responsável pela execução técnica da recolha, normalização e empacotamento da evidência digital.

Esta separação permite distinguir claramente a camada de interface da camada de processamento, evitando concentrar numa única componente tanto a experiência do utilizador como as responsabilidades de aquisição, preservação e verificação da evidência.

## Componentes Principais

### Browser Extension
A browser extension funciona como ponto de entrada operacional do sistema. A sua responsabilidade é identificar o URL ativo no separador corrente, permitir ao utilizador iniciar a captura e apresentar o resultado da operação de forma simples e imediata.

### Local API / Bridge
A comunicação entre a extensão e o motor local é feita através de uma API HTTP local. Esta camada intermédia recebe o pedido da extensão, valida os parâmetros principais e encaminha a execução para o motor de captura.

### Motor Local de Captura e Preservação
O motor local implementa a lógica principal do sistema. Esta componente é responsável pela captura controlada da página, geração dos artefactos, criação do manifest, assinatura, registo da cadeia de custódia, produção dos relatórios e empacotamento final da execução.

### Estrutura de Evidência
Cada execução gera uma pasta própria contendo os artefactos obtidos, os metadados da recolha, o manifest, a assinatura, os relatórios e o pacote ZIP final. Esta estrutura permite repetibilidade, organização e verificação posterior.

## Fluxo de Execução
1. O utilizador abre uma página Web no browser.
2. A browser extension obtém o URL ativo.
3. O utilizador inicia a captura através da extensão.
4. A extensão envia o pedido ao motor local por API HTTP.
5. O motor local executa a captura com Playwright.
6. São gerados screenshot, HTML, PDF, metadados HTTP, logs de consola, HAR e trace.
7. São calculados hashes e produzido o manifest da execução.
8. É registada a cadeia de custódia e gerada a assinatura do manifest.
9. É criado o pacote ZIP final da evidência.
10. O caminho da execução e do ZIP é devolvido à extensão.
11. A integridade pode ser verificada posteriormente sobre a pasta ou sobre o ZIP.

## Justificação Arquitetural
A arquitetura inicialmente implementada como prova de conceito centrava-se numa interface de linha de comandos. Essa abordagem foi útil para validar o núcleo técnico da captura e da preservação, mas apresentava limitações do ponto de vista do produto final, sobretudo ao nível da usabilidade, do contexto de utilização e da clareza arquitetural perante o utilizador-alvo.

A evolução para uma arquitetura com browser extension permitiu aproximar o sistema do cenário real de utilização, em que a recolha de evidência parte do contexto de navegação. Em simultâneo, o reaproveitamento do motor local já desenvolvido permitiu preservar o trabalho técnico realizado e reorganizá-lo numa solução mais coerente, modular e defensável em contexto académico.

## Vantagens da Solução Adotada
- Separação clara entre interface e processamento técnico
- Melhor adequação ao utilizador final
- Reaproveitamento do motor de captura já validado
- Maior coerência entre arquitetura, produto e demonstração
- Facilidade de validação e verificação posterior da integridade

## Limitações Atuais
A solução implementada corresponde a um MVP funcional e, por isso, não cobre todas as dimensões possíveis de uma plataforma de preservação digital. Entre as limitações assumidas estão a ausência de multiutilizador, a inexistência de backend remoto, a falta de integração com mecanismos externos de timestamping qualificado e a simplificação da cadeia de custódia face a cenários forenses mais exigentes.
