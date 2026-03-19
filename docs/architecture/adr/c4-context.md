# C4 - Nível 1 - Diagrama de Contexto

## Sistema principal
Plataforma Modular de Captura e Preservação de Evidência Digital para OSINT

## Utilizador principal
Analista / Estudante  
Interage com o sistema para criar casos, capturar URLs, exportar pacotes e verificar integridade.

## Sistemas externos
### Website público
Fonte externa de conteúdos OSINT.

### Sistema de ficheiros local
Armazena artefactos recolhidos, manifestos e pacotes ZIP.

### Base de dados local SQLite
Guarda metadados estruturados sobre casos, capturas, artefactos e pacotes.

## Relações
- O Analista utiliza a Plataforma
- A Plataforma acede a Websites públicos para recolher conteúdos
- A Plataforma guarda artefactos no sistema de ficheiros
- A Plataforma guarda metadados em SQLite
