# Limitações

A solução implementada corresponde a um MVP funcional e, por isso, assume um conjunto de simplificações compatíveis com o âmbito académico do projeto.

Em primeiro lugar, a solução não suporta multiutilizador nem gestão centralizada de casos, funcionando como ferramenta local orientada a uma execução individual. Em segundo lugar, a comunicação entre a browser extension e o motor técnico é feita por API HTTP local, não existindo nesta fase um backend remoto ou componente de orquestração distribuída.

Adicionalmente, embora a solução produza manifest, assinatura, cadeia de custódia e mecanismos de verificação de integridade, não integra serviços externos de timestamping qualificado nem pretende substituir procedimentos forenses formais em ambientes legais ou periciais mais exigentes.

Estas limitações são consistentes com a natureza de MVP do projeto e definem uma fronteira clara entre a prova funcional implementada e possíveis evoluções futuras.
