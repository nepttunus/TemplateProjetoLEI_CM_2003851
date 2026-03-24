# Arquitetura da Solução

A solução desenvolvida adota uma arquitetura modular composta por duas camadas principais: uma browser extension, responsável pela interação com o utilizador no contexto de navegação, e um motor local de captura e preservação, responsável pela execução técnica da recolha, estruturação e verificação da evidência digital.

Esta separação permite distinguir claramente a componente de interface da componente de processamento. A extensão assume o papel de ponto de entrada operacional do sistema, simplificando a interação do utilizador com a página Web em análise. O motor local concentra as funções de captura controlada, recolha de artefactos, geração de metadados, cálculo de hashes, produção do manifest, assinatura, registo da cadeia de custódia e empacotamento final da execução.

A comunicação entre estas duas camadas é feita através de uma API HTTP local. Quando o utilizador inicia uma captura a partir da extensão, o pedido é enviado ao motor local, que executa a recolha através de Playwright e produz uma pasta de execução estruturada. Essa pasta inclui os artefactos capturados, os metadados da operação, o manifest, a assinatura, os relatórios gerados e o pacote ZIP final.

Do ponto de vista arquitetural, esta abordagem permite melhorar a coerência entre o produto final e o cenário real de utilização. Em vez de depender exclusivamente de uma interface de linha de comandos, a solução passa a partir do contexto de navegação do utilizador, sem perder o reaproveitamento do núcleo técnico já desenvolvido para captura e preservação.
