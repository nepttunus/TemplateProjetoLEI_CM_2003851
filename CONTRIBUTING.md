# Guia de contribuição e workflow

## Conventional Commits

Todas as mensagens de commit devem seguir o standard [Conventional Commits](https://conventionalcommits.org).

### Formato

```
<tipo>: <descrição curta em minúsculas>

[corpo opcional — explicação mais detalhada]

[rodapé opcional — referências a issues]
```

### Tipos obrigatórios

| Tipo | Quando usar |
|------|------------|
| `feat:` | Nova funcionalidade |
| `fix:` | Correcção de bug |
| `docs:` | Alteração de documentação (incluindo README, ADRs, changelog) |
| `refactor:` | Refactoring sem alteração de comportamento |
| `test:` | Adição ou correcção de testes |
| `chore:` | Tarefas de manutenção (dependências, configuração) |

### Exemplos correctos

```
feat: adicionar autenticação por email e password
fix: corrigir validação de formulário no registo
docs: actualizar changelog semana 5
docs: adicionar ADR-003 sobre escolha de base de dados
refactor: extrair lógica de validação para módulo separado
test: adicionar testes unitários ao módulo de autenticação
```

### Exemplos incorrectos

```
update                          ← demasiado vago
fixed bug                       ← sem tipo, passado
WIP                             ← não commitar trabalho incompleto
asjdklasjd                      ← não commitar código não testado com mensagem vazia
```

## Workflow recomendado

1. **Trabalhar em branches** para funcionalidades novas: `git checkout -b feat/nome-da-funcionalidade`
2. **Commits pequenos e frequentes** — um commit por alteração lógica, não por sessão de trabalho
3. **Não commitar código quebrado** — o branch `main` deve estar sempre num estado funcional
4. **Pull request para `main`** quando a funcionalidade estiver completa e testada

## Frequência esperada

O changelog semanal deve reflectir commits regulares ao longo da semana. Um padrão de commits concentrado nos dias imediatamente antes das entregas é uma fragilidade visível no histórico do repositório.
