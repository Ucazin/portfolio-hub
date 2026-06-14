# Guia de Contribuição — PortfolioHUB

Obrigado por considerar contribuir com o **PortfolioHUB**. Este documento define o
fluxo de trabalho, os padrões de versionamento e as regras de colaboração do
repositório. Ele serve tanto para colaboradores externos quanto como
documentação do meu próprio processo de desenvolvimento.

---

## 1. Pré-requisitos

- **Git** instalado e configurado (`git config user.name` e `user.email`).
- **GitHub CLI** (`gh`) — opcional, mas recomendado para abrir PRs pelo terminal.
- Conta no GitHub com **autenticação de dois fatores (2FA) ativada**.
- Python 3.10+ para rodar os projetos da pasta `projetos-academicos/`.

---

## 2. Fluxo de trabalho (Git Flow simplificado)

A branch `main` é **protegida**: ninguém faz push direto nela. Todo trabalho passa
por uma *branch* de feature e um *Pull Request* revisado.

```
main (protegida, sempre estável e publicável)
 └── feat/nome-da-feature      ← novas funcionalidades
 └── fix/descricao-do-bug      ← correções
 └── docs/o-que-foi-documentado ← documentação
 └── chore/tarefa-de-config    ← configuração/manutenção
```

### Passo a passo

```bash
# 1. Atualize sua main local
git checkout main
git pull origin main

# 2. Crie uma branch a partir da main
git checkout -b feat/minha-contribuicao

# 3. Faça suas alterações e commits seguindo o padrão (ver seção 3)
git add .
git commit -m "feat: descreve a mudança no imperativo"

# 4. Envie a branch
git push -u origin feat/minha-contribuicao

# 5. Abra um Pull Request para a main
gh pr create --base main --fill
```

---

## 3. Padrão de commits — Conventional Commits

Todas as mensagens de commit seguem o padrão
[Conventional Commits](https://www.conventionalcommits.org/pt-br/):

| Prefixo | Quando usar |
|---------|-------------|
| `feat:`  | Nova funcionalidade |
| `fix:`   | Correção de bug |
| `docs:`  | Apenas documentação |
| `style:` | Formatação, espaçamento (sem mudança de lógica) |
| `refactor:` | Refatoração sem mudar comportamento |
| `test:`  | Adição/ajuste de testes |
| `chore:` | Configuração, build, dependências, tarefas gerais |
| `ci:`    | Mudanças em pipelines de CI (GitHub Actions) |

**Exemplos:**

```
feat: adicionar projeto 04 de séries temporais
docs: corrigir link quebrado no README principal
chore: ativar Dependabot para os projetos Python
```

---

## 4. Versionamento — SemVer

O repositório segue [Versionamento Semântico](https://semver.org/lang/pt-BR/)
no formato `MAJOR.MINOR.PATCH`:

- **MAJOR** — mudança estrutural grande (ex.: `v2.0.0` = implantação em produção).
- **MINOR** — novo projeto ou funcionalidade compatível.
- **PATCH** — correção pontual.

Cada release relevante recebe uma **tag** anotada e uma **Release** no GitHub.

---

## 5. Regras do Pull Request

Para ser mergeado na `main`, todo PR precisa:

1. ✅ Passar nos **status checks** do GitHub Actions (`Validar estrutura` e `Validar HTML`).
2. ✅ Ter **pelo menos 1 aprovação** de revisão (`required reviews`).
3. ✅ Ter as **conversas resolvidas** (comentários de review respondidos).
4. ✅ Respeitar o **CODEOWNERS** (revisão do dono do código quando aplicável).
5. ✅ Manter **histórico linear** (sem merge commits cruzados — usamos *squash*).

> Como o repositório hoje tem um único mantenedor, o merge pode ser feito com
> *override* de administrador quando não há um segundo revisor disponível. As
> regras de proteção permanecem ativas e documentadas como boa prática.

---

## 6. Reportando problemas

Use os **templates de issue** disponíveis em *New issue*:

- 🐛 **Bug report** — para erros e comportamentos inesperados.
- ✨ **Feature request** — para sugestões de novos projetos ou melhorias.

---

## 7. Código de conduta

Ao contribuir, você concorda em seguir o
[Código de Conduta](CODE_OF_CONDUCT.md) do projeto.

---

Mantenedor: **Lucca Mariz** ([@Ucazin](https://github.com/Ucazin))
