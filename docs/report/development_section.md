# Desenvolvimento e Evolução da Solução

A primeira iteração do projeto foi desenvolvida sob a forma de uma prova de conceito orientada a linha de comandos. Essa abordagem permitiu validar rapidamente o núcleo técnico do sistema, nomeadamente a captura de páginas Web, a geração de screenshot, HTML e PDF, a recolha de metadados, o cálculo de hashes, a produção do manifest, o registo de eventos de cadeia de custódia e a verificação posterior da integridade.

Apesar de funcional, essa primeira abordagem apresentava limitações enquanto produto final. Em particular, a utilização exclusiva de uma CLI não refletia da forma mais adequada o contexto real de utilização da solução, nem favorecia uma interação natural com o cenário OSINT que o projeto pretendia suportar.

Na sequência da reavaliação da arquitetura, a solução foi reformulada para separar a interface do utilizador do motor técnico de captura e preservação. O núcleo desenvolvido inicialmente foi preservado e reorganizado como motor local, enquanto a interação passou a ser feita através de uma browser extension. Desta forma, a evolução do projeto não correspondeu a uma substituição integral da implementação anterior, mas sim a um reposicionamento arquitetural do trabalho já realizado.

Esta transição permitiu manter a base técnica já validada, ao mesmo tempo que aproximou o sistema do cenário real de utilização. O resultado é uma solução mais coerente, modular e defensável, em que o utilizador inicia a captura a partir do browser e o motor local trata da preservação e estruturação da evidência digital.
