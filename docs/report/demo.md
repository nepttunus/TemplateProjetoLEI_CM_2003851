# Roteiro de Demonstração

## Objetivo
Demonstrar que a solução permite iniciar uma captura a partir do browser, gerar um pacote estruturado de evidência e verificar posteriormente a sua integridade.

## Sequência da Demonstração
1. Abrir uma página Web de exemplo no browser.
2. Abrir a browser extension.
3. Mostrar que a extensão identifica o URL ativo.
4. Iniciar a captura através do botão disponível no popup.
5. Mostrar o retorno do motor local, incluindo a pasta de execução e o caminho do ZIP.
6. Abrir a pasta gerada em `output/`.
7. Mostrar os artefactos produzidos:
   - screenshot
   - HTML
   - PDF
   - metadados
   - manifest
   - assinatura
   - cadeia de custódia
   - relatórios
   - ZIP final
8. Executar a verificação da integridade sobre a pasta da execução.
9. Executar a verificação da integridade sobre o ZIP final.
10. Confirmar que o sistema devolve estado `ok` em ambos os casos.

## Mensagem Principal da Demonstração
A demonstração deve evidenciar que a solução não se limita à recolha visual da página, mas produz um conjunto estruturado de artefactos verificáveis, preservando contexto, integridade e rastreabilidade mínima da execução.
