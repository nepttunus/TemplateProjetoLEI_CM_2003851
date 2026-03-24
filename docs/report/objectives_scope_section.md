# Objetivos e Âmbito

O objetivo principal do projeto consiste em desenvolver uma solução capaz de capturar e preservar evidência digital web em contexto OSINT, garantindo uma estrutura mínima de integridade, rastreabilidade e organização dos artefactos obtidos.

A solução foi concebida para permitir que o utilizador inicie a recolha diretamente a partir do browser, delegando a execução técnica da captura e preservação para um motor local dedicado. O resultado esperado é a geração de uma pasta de execução estruturada e de um pacote ZIP final contendo os artefactos recolhidos, os metadados da operação, o manifest, a assinatura e os elementos necessários à verificação posterior da integridade.

No âmbito do MVP, incluem-se a recolha do URL ativo, a captura de screenshot, HTML e PDF, a geração de metadados, o cálculo de hashes, a produção do manifest, a criação da cadeia de custódia, a assinatura e o empacotamento final. Ficam fora do âmbito desta versão funcionalidades como multiutilizador, backend remoto, timestamping qualificado, integração com serviços externos e suporte a recolha em lote de múltiplos alvos.
