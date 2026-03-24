# Evolução da Solução

A primeira iteração do projeto foi desenvolvida sob a forma de uma prova de conceito orientada a linha de comandos. Essa abordagem permitiu validar rapidamente o núcleo técnico da solução, nomeadamente a captura de páginas Web, a recolha de artefactos, a geração de metadados, o cálculo de hashes, a produção do manifest e a verificação posterior da integridade.

No entanto, após análise crítica da solução e reavaliação do enquadramento do projeto, tornou-se claro que a apresentação do sistema como ferramenta CLI não representava a forma mais adequada de materializar o produto final. Apesar de funcional do ponto de vista técnico, essa abordagem não refletia da melhor forma o contexto de utilização nem a interação esperada para o público-alvo.

A reformulação arquitetural consistiu, assim, em preservar o motor local já implementado e reposicioná-lo como componente interna de captura e preservação, acrescentando uma browser extension como camada de interação com o utilizador. Desta forma, o projeto passou de uma ferramenta predominantemente técnica para uma solução mais alinhada com o cenário real de recolha de evidência a partir do browser.

Esta transição não implicou o abandono do trabalho anteriormente realizado. Pelo contrário, o núcleo técnico da prova de conceito foi reutilizado como motor local, sendo reorganizado para funcionar atrás de uma interface mais adequada e coerente com os objetivos do projeto. Assim, a evolução da solução representou uma mudança de arquitetura e de produto, e não uma substituição integral da implementação já existente.
