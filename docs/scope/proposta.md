# Proposta de Projeto

## Título
Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

## Estudante
Carlos Marques (2003851)

## Orientador
Pedro Duarte Pestana

## Sinopse
Em contexto de segurança informática e resposta a incidentes, é comum recorrer a fontes públicas na Internet para recolher informação relevante sobre domínios, páginas, perfis, notícias ou outros elementos com valor de evidência digital. No entanto, esta recolha é muitas vezes feita de forma manual e pouco estruturada, o que dificulta a preservação da integridade dos artefactos, a rastreabilidade do processo e a sua validação posterior. O problema que este projeto procura resolver é a ausência de um processo simples e consistente para capturar e preservar evidência OSINT de forma tecnicamente rigorosa.

A solução proposta consiste no desenvolvimento de uma plataforma modular, implementada em Python, capaz de criar casos, capturar conteúdos a partir de URLs, guardar artefactos relevantes como HTML e screenshots, associar metadados mínimos e gerar um pacote de evidência com manifesto JSON e hashes SHA-256. A proposta distingue-se por procurar um equilíbrio entre simplicidade, reprodutibilidade e preservação de integridade, permitindo demonstrar um fluxo completo de recolha e validação de evidência digital em ambiente de laboratório.

O resultado esperado é um MVP funcional que permita criar um caso, recolher evidência a partir de uma URL válida, gerar um pacote ZIP com manifesto e hashes e verificar automaticamente se a integridade da evidência se mantém ou se foi comprometida por alteração deliberada de um artefacto. O projeto será considerado bem-sucedido se estes critérios forem cumpridos e demonstrados através de testes funcionais e testes negativos em ambiente controlado.

## MVP e critérios de aceitação

### 1. Criação de caso
**Descrição**  
O sistema deve permitir criar um caso novo, identificado de forma única, ao qual serão associadas as capturas realizadas.

**Critério de aceitação**  
Dado um título válido, o sistema cria um identificador único de caso, gera a estrutura de diretórios correspondente e regista o caso na camada de persistência.

### 2. Captura de URL
**Descrição**  
O sistema deve permitir capturar uma página web pública a partir de uma URL fornecida pelo utilizador.

**Critério de aceitação**  
Dada uma URL válida e acessível, o sistema gera pelo menos um ficheiro HTML e uma imagem de screenshot, guardando ambos na pasta do caso e registando a operação com timestamp e URL de origem.

### 3. Registo de metadados
**Descrição**  
Cada captura deve ficar associada a metadados mínimos que permitam contextualizar a evidência recolhida.

**Critério de aceitação**  
Após uma captura bem-sucedida, o sistema regista pelo menos a URL, a data e hora da recolha, o identificador do caso e o conjunto de artefactos gerados.

### 4. Geração de manifesto
**Descrição**  
O sistema deve produzir um manifesto estruturado em JSON com a descrição dos artefactos e respetivos hashes.

**Critério de aceitação**  
Dado um caso com pelo menos uma captura concluída, o sistema gera um ficheiro `manifest.json` contendo a lista dos artefactos, os seus caminhos relativos, hashes SHA-256 e metadados essenciais do caso.

### 5. Exportação de pacote de evidência
**Descrição**  
O sistema deve ser capaz de gerar um pacote final de evidência para preservação e transporte.

**Critério de aceitação**  
Dado um caso válido, o sistema cria um ficheiro ZIP contendo os artefactos recolhidos e o manifesto JSON, mantendo coerência entre o conteúdo do pacote e os metadados registados.

### 6. Verificação de integridade
**Descrição**  
O sistema deve permitir verificar se os artefactos incluídos num pacote continuam íntegros.

**Critério de aceitação**  
Dado um pacote não alterado, o sistema devolve resultado positivo de integridade. Dado um pacote em que um artefacto tenha sido alterado, o sistema devolve resultado negativo e identifica a discrepância.

## Stack tecnológica prevista
- **Python** como linguagem principal, pela simplicidade, legibilidade e adequação ao problema
- **Playwright** para captura de páginas web e geração de screenshots
- **SQLite** para armazenamento simples de metadados no MVP
- **JSON** para manifesto de evidência
- **SHA-256** para verificação de integridade
- **pytest** para testes unitários e de integração

## Esboço de arquitetura
A arquitetura inicial será composta por um núcleo de linha de comandos que orquestra quatro componentes principais:
- gestão de casos
- motor de captura
- construtor do pacote de evidência
- módulo de verificação de integridade

O sistema interage com o utilizador através de uma CLI, com a Internet como fonte externa de conteúdos públicos e com armazenamento local para metadados e artefactos.

## Calendário individual detalhado

### Semana 1
**17 a 23 de março**  
Definição final da sinopse, do MVP e dos critérios de aceitação. Estruturação do repositório GitHub e organização da documentação inicial.

### Semana 2
**24 a 30 de março**  
Levantamento de requisitos funcionais e não funcionais com priorização MoSCoW. Produção do diagrama C4 nível 1 e desenho inicial do modelo de dados.

### Semanas 3 e 4
**31 de março a 11 de abril**  
Preparação do ambiente de desenvolvimento em Python. Estruturação da aplicação e validação inicial da integração com Playwright.

### Semanas 5 e 6
**14 a 25 de abril**  
Implementação do núcleo do MVP com criação de casos, captura de URL, geração de artefactos, manifesto e hashes.

### Semana 7
**28 de abril a 2 de maio**  
Está prevista uma janela de disponibilidade reduzida por motivo pessoal já identificado. Por esse motivo, a implementação principal do núcleo do MVP será concentrada antes deste período, ficando para esta semana tarefas de consolidação e revisão.

### Semana 8
**5 e 6 de maio**  
Preparação e entrega do relatório intercalar, com foco na documentação da arquitetura, estado de implementação e planeamento seguinte.

### Semanas 9 e 10
**7 a 16 de maio**  
Implementação da exportação do pacote ZIP e do módulo de verificação de integridade. Início dos testes unitários e de integração.

### Semanas 11 e 12
**19 a 30 de maio**  
Consolidação do MVP. Execução de testes funcionais, negativos e de desempenho. Recolha de capturas de ecrã e exemplos de execução para o relatório.

### Semana 13
**2 a 6 de junho**  
Validação dos critérios de aceitação definidos na proposta. Revisão da arquitetura e ajustamentos finais ao sistema.

### Semana 14
**9 a 13 de junho**  
Redação do relatório final, revisão bibliográfica e preparação dos anexos e evidências.

### Semana 15
**16 a 20 de junho**  
Revisão global do repositório, do relatório e das decisões de arquitetura. Preparação para submissão e defesa.

### Semana 16
**24 de junho**  
Submissão do relatório final, código e artefactos associados.

## Nota final
Todo o desenvolvimento e validação serão realizados em ambiente de laboratório, com dados simulados e sem utilização de informação sensível ou confidencial.
