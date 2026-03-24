# Implementação do MVP

A implementação do MVP foi organizada em três componentes principais: browser extension, API local e motor local de captura e preservação.

A browser extension constitui a camada de interação com o utilizador. A sua função consiste em obter o URL ativo no browser, permitir o arranque da captura e apresentar o resultado devolvido pelo motor local, incluindo a pasta de execução gerada e o caminho do pacote ZIP final.

A API local funciona como camada intermédia entre a extensão e o motor técnico. Esta componente recebe os pedidos de captura iniciados a partir do browser e encaminha-os para o serviço interno responsável pela execução da recolha e preservação.

O motor local implementa o núcleo técnico da solução. A captura é efetuada com recurso a Playwright, sendo gerados screenshot, HTML, PDF, metadados HTTP, registos de consola, HAR e trace. Sobre os artefactos obtidos são depois produzidos o manifest, a assinatura, a cadeia de custódia e os relatórios de apoio, culminando na criação de um pacote ZIP final.

A implementação permitiu reutilizar o núcleo técnico inicialmente desenvolvido em formato CLI, reorganizando-o de forma a funcionar como componente interna de uma solução mais modular e adequada ao produto final pretendido.
