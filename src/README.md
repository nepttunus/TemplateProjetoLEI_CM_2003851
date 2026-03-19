# Código-fonte

Organizar o código-fonte segundo a arquitectura documentada em `docs/architecture/`.

## Estrutura sugerida

A estrutura exacta depende da stack e da arquitectura escolhida. O princípio é que **a organização das pastas deve reflectir a arquitectura documentada no C4** — alguém que leia o C4 deve conseguir encontrar o código correspondente a cada contentor sem esforço.

### Exemplo — aplicação web com frontend e backend separados

```
src/
  frontend/        ← contentor "Web App" do C4
    components/
    pages/
    services/
  backend/         ← contentor "API" do C4
    routes/
    models/
    services/
  database/        ← migrações, seeds, schemas
```

### Exemplo — aplicação mobile

```
src/
  lib/             ← lógica de negócio
  screens/         ← ecrãs da aplicação
  services/        ← integração com APIs externas
  models/          ← modelos de dados
```

## Notas

- Incluir um `.env.example` com as variáveis de ambiente necessárias (sem valores reais).
- Não incluir no repositório: ficheiros `.env`, credenciais, chaves de API, dados reais de utilizadores.
- Usar `.gitignore` adequado à stack — [gitignore.io](https://gitignore.io) gera automaticamente.
