<div align="center">

# Documento de Implantação — PortfolioHUB + IA Gemini

### Entrega Final · Bootcamp 1

**Lucca Coelho Mendes de Mariz Dantas Del Bosco** (Lucca Mariz)
Ciência de Dados e Machine Learning — Centro Universitário de Brasília (CEUB)
Campus Asa Norte · 2026

**GitHub:** [@Ucazin](https://github.com/Ucazin) ·
**Repositório:** [github.com/Ucazin/portfolio-hub](https://github.com/Ucazin/portfolio-hub) ·
**Produção (Pages):** [ucazin.github.io/portfolio-hub](https://ucazin.github.io/portfolio-hub/)

Data da implantação: **14/06/2026**

</div>

---

> **Como usar este documento:** ele já está pronto para virar PDF. Onde houver
> `[PREENCHER: ...]` é conteúdo pessoal seu (links, nomes, datas). Onde houver
> `[📷 COLAR PRINT: ...]` você deve inserir uma captura de tela. Onde houver
> `🤖 PROMPT GEMINI` está a pergunta exata que você deve fazer ao Google Gemini e
> colar o print da resposta logo abaixo, cumprindo o requisito de uso da IA.

---

## Sumário

1. [Planejamento da Implantação](#1-planejamento-da-implantação)
2. [Configuração Inicial e Integração com GitHub](#2-configuração-inicial-e-integração-com-github)
3. [Gestão de Usuários e Segurança](#3-gestão-de-usuários-e-segurança)
4. [Compartilhamento e Controle de Acesso com GitHub](#4-compartilhamento-e-controle-de-acesso-com-github)
5. [Finalização da Integração e Testes](#5-finalização-da-integração-e-testes)
6. [Revisão Final e Apresentação](#6-revisão-final-e-apresentação)
- [Apêndice A — Mapa de prints](#apêndice-a--mapa-de-prints)
- [Apêndice B — Prompts do Google Gemini](#apêndice-b--prompts-do-google-gemini)

---

## 1. Planejamento da Implantação

### 1.1 Objetivo

Implantar o **PortfolioHUB** — repositório que centraliza meus projetos
acadêmicos e pessoais — em um ambiente de produção real, versionado, seguro e
colaborativo no GitHub, publicado via GitHub Pages, e usando o **Google Gemini**
como ferramenta de apoio ao longo de todo o processo de planejamento e execução.

Esta é a terceira e última etapa de um trabalho em três fases:

| Etapa | Entrega | Status |
|-------|---------|--------|
| Inicial | Portfólio Profissional Digital (PDF, 6 seções) | ✅ Concluída |
| Intermediária | Repositório com versionamento + GitHub Pages | ✅ Concluída (`v1.0.0`) |
| **Final** | **Implantação em produção + IA Gemini** | ✅ **Esta entrega (`v2.0.0`)** |

### 1.2 Escopo da implantação

**Dentro do escopo:**
- Ambiente dedicado de desenvolvimento (Git + GitHub CLI autenticado).
- Repositório organizado com armazenamento estruturado dos projetos.
- Gestão de usuários e papéis (roles) de acesso.
- Políticas de segurança (branch protection, 2FA, Dependabot, secret scanning, `.gitignore`).
- Fluxo de colaboração documentado (branches, Pull Requests, code review).
- Pipeline de testes/integração contínua (GitHub Actions).
- Publicação em produção (GitHub Pages) e versionamento de release.

**Fora do escopo:**
- Migração para servidor próprio ou nuvem paga (o GitHub Pages é o ambiente de produção).
- Backend ou banco de dados (o portfólio é estático).

### 1.3 Arquitetura da solução

```
            ┌──────────────────────────────────────────────┐
            │              AMBIENTE LOCAL                    │
            │   Git + GitHub CLI (gh) autenticado            │
            │   Conta: Ucazin                                │
            └───────────────────┬──────────────────────────┘
                                │  git push / gh pr
                                ▼
            ┌──────────────────────────────────────────────┐
            │                  GITHUB                        │
            │  Repositório: Ucazin/portfolio-hub (público)   │
            │  • Branch main PROTEGIDA                       │
            │  • Pull Requests + Code Review (CODEOWNERS)    │
            │  • GitHub Actions (CI) → testes automáticos    │
            │  • Dependabot + Secret Scanning                │
            └───────────────────┬──────────────────────────┘
                                │  deploy automático
                                ▼
            ┌──────────────────────────────────────────────┐
            │           PRODUÇÃO — GITHUB PAGES              │
            │   https://ucazin.github.io/portfolio-hub/      │
            └──────────────────────────────────────────────┘
```

### 1.4 Plano detalhado de etapas

| # | Etapa | Ferramenta | Resultado esperado |
|---|-------|-----------|--------------------|
| 1 | Planejar a implantação com apoio do Gemini | Google Gemini | Plano validado e checklist |
| 2 | Preparar ambiente dedicado (Git + gh autenticado) | Git, GitHub CLI | Ambiente pronto |
| 3 | Organizar repositório e armazenamento dos projetos | Git/GitHub | Estrutura de pastas clara |
| 4 | Configurar gestão de usuários e segurança | GitHub + gh CLI | Acesso controlado e seguro |
| 5 | Documentar fluxo de colaboração e versionamento | Git/PR/Review | Colaboração rastreável |
| 6 | Configurar CI e preparar produção | GitHub Actions, Pages | Deploy testado |
| 7 | Revisão final, release e apresentação | GitHub Releases, YouTube | Entrega concluída |

### 1.5 Uso do Google Gemini no planejamento

> 🤖 **PROMPT GEMINI 1 — Plano de implantação**
>
> *"Sou estudante de Ciência de Dados e vou implantar meu portfólio de projetos
> num repositório GitHub público chamado portfolio-hub. Preciso de um plano de
> implantação profissional cobrindo: organização do repositório, gestão de
> usuários e permissões, políticas de segurança (branch protection, 2FA,
> Dependabot), fluxo de colaboração com Pull Requests, integração contínua com
> GitHub Actions e publicação em produção via GitHub Pages. Me dê um plano em
> etapas, com boas práticas para cada uma."*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 1 — plano de implantação]

**Como usei a resposta:** [PREENCHER: escreva 2–3 linhas dizendo o que você
aproveitou da resposta do Gemini — ex.: "o Gemini reforçou a importância de
aplicar o princípio do menor privilégio e de exigir review nos PRs, o que adotei
na seção 3 e 4".]

---

## 2. Configuração Inicial e Integração com GitHub

### 2.1 Ambiente dedicado

O ambiente de desenvolvimento foi preparado com as ferramentas oficiais:

| Ferramenta | Função | Verificação |
|-----------|--------|-------------|
| **Git** | Controle de versão local | `git --version` |
| **GitHub CLI (`gh`)** | Integração com o GitHub pelo terminal | `gh --version` |
| Conta GitHub `Ucazin` | Hospedagem remota | `gh auth status` |

**Autenticação verificada** (saída real do ambiente):

```text
github.com
  ✓ Logged in to github.com account Ucazin (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

[📷 COLAR PRINT: terminal mostrando `gh auth status` autenticado como Ucazin]

### 2.2 Identidade do Git

```bash
git config user.name   "Lucca Mariz"
git config user.email  "luccamariz01@gmail.com"
```

### 2.3 Repositório e integração

O repositório `Ucazin/portfolio-hub` já estava versionado localmente e
conectado ao remoto. A integração foi confirmada por:

```bash
git remote -v
# origin  https://github.com/Ucazin/portfolio-hub.git (fetch)
# origin  https://github.com/Ucazin/portfolio-hub.git (push)
```

### 2.4 Armazenamento e organização dos projetos

A estrutura de pastas separa projetos por origem e concentra documentação e
infraestrutura, facilitando a manutenção e a colaboração:

```
portfolio-hub/
├── index.html                  ← Página principal (produção / GitHub Pages)
├── assets/                     ← CSS, JS e imagens da vitrine
├── projetos-academicos/        ← Projetos da graduação
│   ├── 01-analise-exploratoria-vendas/
│   └── 02-classificacao-iris-ml/
├── projetos-pessoais/          ← Projetos pessoais
│   └── 03-dashboard-covid-visualizacao/
├── slides/                     ← Apresentação interativa
├── docs/                       ← Documentação geral
│   ├── apresentacao.md
│   ├── roteiro-video.md
│   └── implantacao/            ← Documentação desta Entrega Final
├── .github/                    ← Governança, CI e templates
│   ├── workflows/ci.yml        ← Pipeline de testes
│   ├── ISSUE_TEMPLATE/         ← Templates de issue
│   ├── CODEOWNERS              ← Revisores obrigatórios
│   ├── dependabot.yml          ← Atualização de dependências
│   └── pull_request_template.md
├── CONTRIBUTING.md             ← Guia de contribuição
├── SECURITY.md                 ← Política de segurança
├── CODE_OF_CONDUCT.md          ← Código de conduta
├── README.md                   ← Documento de boas-vindas
├── LICENSE                     ← Licença MIT
└── .gitignore                  ← Higiene de arquivos
```

[📷 COLAR PRINT: árvore de pastas do repositório no GitHub OU saída de `git ls-files`]

> 🤖 **PROMPT GEMINI 2 — Organização do repositório**
>
> *"Qual a melhor forma de organizar as pastas de um repositório de portfólio
> que reúne projetos acadêmicos e pessoais de ciência de dados, para que fique
> profissional e fácil de manter? Que arquivos de governança (README,
> CONTRIBUTING, SECURITY, LICENSE) não podem faltar?"*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 2 — organização do repositório]

---

## 3. Gestão de Usuários e Segurança

### 3.1 Gestão de usuários e papéis (roles)

O GitHub oferece cinco níveis de permissão por repositório, aplicados segundo o
**princípio do menor privilégio** (cada pessoa recebe o mínimo necessário):

| Papel (role) | O que permite | Quando usar |
|--------------|---------------|-------------|
| **Read** | Clonar e ler | Visitantes, professores avaliadores |
| **Triage** | Gerenciar issues/PRs sem escrever código | Moderadores |
| **Write** | Push em branches e abrir PRs | Colaboradores ativos |
| **Maintain** | Gerenciar o repositório sem acesso destrutivo | Coordenadores |
| **Admin** | Controle total (settings, segurança) | Dono do repositório |

**Convite de colaborador via GitHub CLI** (comando pronto):

```bash
# Substitua USUARIO pelo @ do colaborador e escolha o permission:
# pull (Read) | triage | push (Write) | maintain | admin
gh api -X PUT repos/Ucazin/portfolio-hub/collaborators/USUARIO -f permission=push
```

Para esta entrega individual, o controle de acesso foi configurado e documentado;
o convite de um colaborador de demonstração pode ser feito com o comando acima.

[📷 COLAR PRINT: aba **Settings → Collaborators and teams** mostrando os papéis
(ou o resultado de um convite enviado, se você convidar alguém)]

[PREENCHER: se você convidou alguém (uma 2ª conta sua ou um colega), escreva
aqui o @usuário e o papel atribuído. Ex.: "Convidei @colega-teste com papel
Write (push) para demonstrar a colaboração."]

### 3.2 Políticas de segurança aplicadas

As boas práticas de segurança abaixo foram efetivamente configuradas neste
repositório (detalhes técnicos no arquivo [`SECURITY.md`](../../SECURITY.md)):

| Política | Como foi aplicada | Onde |
|----------|-------------------|------|
| Autenticação 2FA | Ativada na conta do mantenedor | Conta GitHub |
| Proteção da branch `main` | PR obrigatório + 1 review + checks + histórico linear | Settings → Branches |
| Higiene de segredos | `.gitignore` bloqueia `.env`, chaves, bancos, credenciais | `.gitignore` |
| Secret scanning + push protection | Habilitados (repo público) | Settings → Code security |
| Alertas de dependências | Dependabot alerts ativado | Settings → Code security |
| Atualização automática | `dependabot.yml` monitorando `pip` e `github-actions` | `.github/dependabot.yml` |
| Menor privilégio | Papéis mínimos por colaborador | Settings → Collaborators |

[📷 COLAR PRINT: aba **Settings → Code security** mostrando Dependabot e Secret
scanning habilitados]

[📷 COLAR PRINT: tela de **2FA ativado** na sua conta
(Settings da conta → Password and authentication). **Não mostre os códigos de
recuperação.**]

> 🤖 **PROMPT GEMINI 3 — Boas práticas de segurança**
>
> *"Quais são as boas práticas de segurança recomendadas para um repositório
> público no GitHub? Quero entender branch protection, autenticação de dois
> fatores, secret scanning, Dependabot e o princípio do menor privilégio na
> gestão de colaboradores."*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 3 — boas práticas de segurança]

---

## 4. Compartilhamento e Controle de Acesso com GitHub

### 4.1 Controle de versão

O versionamento segue padrões profissionais:

- **Conventional Commits** — mensagens padronizadas (`feat:`, `fix:`, `docs:`,
  `chore:`, `ci:`), tornando o histórico legível.
- **Versionamento Semântico (SemVer)** — `v1.0.0` marcou a entrega intermediária;
  `v2.0.0` marca esta implantação em produção.
- **Branches por finalidade** — `feat/`, `fix/`, `docs/`, `chore/`.

Histórico de commits (exemplo real do repositório):

```text
feat: adicionar apresentação interativa em slides HTML no GitHub Pages
docs: adicionar documento de apresentação e roteiro do vídeo
feat: adicionar site principal do GitHub Pages com design dark tech responsivo
feat: adicionar projeto pessoal 03 — dashboard COVID interativo com Chart.js
feat: adicionar projeto acadêmico 02 — classificação Iris com scikit-learn
```

[📷 COLAR PRINT: saída de `git log --oneline` OU a aba **Commits** do GitHub]

### 4.2 Fluxo de colaboração (documentado e demonstrado)

A colaboração no PortfolioHUB segue um fluxo baseado em Pull Requests:

```
1. Criar branch de feature          →  git checkout -b feat/implantacao-producao
2. Commitar seguindo o padrão        →  git commit -m "feat: ..."
3. Enviar a branch                   →  git push -u origin feat/implantacao-producao
4. Abrir Pull Request                →  gh pr create --base main --fill
5. CI roda automaticamente           →  GitHub Actions valida estrutura e HTML
6. Code review (CODEOWNERS)          →  revisão obrigatória antes do merge
7. Merge na main protegida           →  squash + branch deletada
8. Deploy automático                 →  GitHub Pages publica a nova versão
```

**Este fluxo foi efetivamente executado nesta entrega:** toda a configuração de
governança, segurança e CI foi adicionada por meio de uma branch
`feat/implantacao-producao` e de um Pull Request real, revisado e mergeado na
`main` protegida.

**Pull Request #1** — https://github.com/Ucazin/portfolio-hub/pull/1
(branch `feat/implantacao-producao`, CI verde, mergeado na `main` protegida).
Um segundo PR (`feat/ajuste-dependabot-e-links`) ajustou o Dependabot e preencheu
estes links, reforçando que o fluxo de colaboração é repetível.

[📷 COLAR PRINT: a página do **Pull Request** mostrando os checks verdes do CI e
o merge realizado]

### 4.3 Controle de acesso ao código

- **CODEOWNERS** (`.github/CODEOWNERS`) define `@Ucazin` como revisor obrigatório
  de todo o repositório — nenhuma mudança entra sem passar pela revisão do dono.
- **Branch protection** impede push direto na `main` e exige PR aprovado.
- **Repositório público** com licença MIT permite leitura/clonagem por qualquer
  pessoa, mas a escrita é controlada por papéis.

> 🤖 **PROMPT GEMINI 4 — Fluxo de colaboração com Pull Requests**
>
> *"Explique o fluxo profissional de colaboração no GitHub usando branches e
> Pull Requests, com code review e branch protection. Por que é melhor do que
> dar push direto na main? Como o arquivo CODEOWNERS ajuda nesse controle?"*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 4 — fluxo de colaboração]

---

## 5. Finalização da Integração e Testes

### 5.1 Integração contínua (GitHub Actions)

Foi criado o pipeline `.github/workflows/ci.yml`, que roda automaticamente a
cada push na `main` e em todo Pull Request. Ele possui dois jobs de teste:

| Job | O que valida |
|-----|--------------|
| **Validar estrutura** | Confere se os arquivos e pastas obrigatórios existem (README, LICENSE, index.html, projetos, docs, governança). |
| **Validar HTML** | Faz parsing de todos os `.html` e falha se houver tag `<html>` sem fechamento ou erro de sintaxe. |

Esses jobs são **status checks obrigatórios**: a `main` só aceita merge quando
ambos passam (verde), garantindo que nada quebrado chegue à produção.

[📷 COLAR PRINT: aba **Actions** do GitHub mostrando a execução do CI com os dois
jobs verdes ✅]

### 5.2 Ambiente de produção

A produção é o **GitHub Pages**, que faz deploy automático da branch `main`:

- **URL de produção:** https://ucazin.github.io/portfolio-hub/
- **Status atual:** publicado e no ar (`built`).
- A cada merge na `main`, o Pages republica automaticamente a versão mais recente.

[📷 COLAR PRINT: o site em produção aberto no navegador, mostrando a URL
`ucazin.github.io/portfolio-hub`]

### 5.3 Testes realizados

| Teste | Método | Resultado |
|-------|--------|-----------|
| Estrutura do repositório | Job `Validar estrutura` (CI) | ✅ |
| Integridade dos HTML | Job `Validar HTML` (CI) | ✅ |
| Publicação em produção | Acesso à URL do GitHub Pages | ✅ |
| Proteção da branch | Tentativa de push direto bloqueada | ✅ |
| Fluxo de PR | PR aberto, revisado e mergeado | ✅ |

### 5.4 Release de produção

A implantação foi marcada com a tag/Release **`v2.0.0`**, sinalizando a entrada
em produção (mudança MAJOR em relação à `v1.0.0` da entrega intermediária).

**Release v2.0.0** — https://github.com/Ucazin/portfolio-hub/releases/tag/v2.0.0

[📷 COLAR PRINT: a página da **Release v2.0.0** no GitHub]

> 🤖 **PROMPT GEMINI 5 — CI/CD e preparação para produção**
>
> *"O que é integração contínua (CI) e como o GitHub Actions ajuda a preparar um
> projeto para produção? Que tipos de testes simples eu posso rodar
> automaticamente em um portfólio estático antes de publicar no GitHub Pages?"*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 5 — CI/CD e produção]

---

## 6. Revisão Final e Apresentação

### 6.1 Checklist de revisão final

| Item | Status |
|------|--------|
| Repositório público e organizado | ✅ |
| Documentação completa (README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT) | ✅ |
| Gestão de usuários e papéis documentada | ✅ |
| Políticas de segurança aplicadas | ✅ |
| Branch protection ativa na `main` | ✅ |
| Fluxo de colaboração com PR demonstrado | ✅ |
| CI (GitHub Actions) funcionando | ✅ |
| Produção (GitHub Pages) no ar | ✅ |
| Release `v2.0.0` publicada | ✅ |
| Uso do Google Gemini documentado | ✅ (prints nas seções 1–5) |
| Vídeo de apresentação no YouTube | [PREENCHER: ✅ após gravar] |

### 6.2 Links finais da entrega

| Recurso | Link |
|---------|------|
| Repositório | https://github.com/Ucazin/portfolio-hub |
| Produção (GitHub Pages) | https://ucazin.github.io/portfolio-hub/ |
| Pull Request da implantação | https://github.com/Ucazin/portfolio-hub/pull/1 |
| Release v2.0.0 | https://github.com/Ucazin/portfolio-hub/releases/tag/v2.0.0 |
| Vídeo no YouTube | [PREENCHER: link do vídeo] |
| LinkedIn | https://www.linkedin.com/in/lucca-mariz/ |

### 6.3 Vídeo de apresentação

O vídeo de até 5 minutos, publicado no YouTube, percorre as etapas da
implantação. O roteiro completo está em
[`roteiro-video-final.md`](./roteiro-video-final.md).

[PREENCHER: link do vídeo no YouTube]

### 6.4 Conclusão e aprendizados

[PREENCHER: escreva 4–6 linhas com sua reflexão pessoal. Sugestões do que
abordar: o que você aprendeu sobre implantação e governança no GitHub; como o
Google Gemini ajudou em cada etapa; qual boa prática de segurança você achou
mais importante; e quais são os próximos passos do PortfolioHUB.]

> 🤖 **PROMPT GEMINI 6 — Revisão final**
>
> *"Revise este plano de implantação de um portfólio no GitHub e aponte se está
> faltando alguma boa prática importante de organização, segurança ou
> colaboração. [cole aqui um resumo do que você fez]"*

[📷 COLAR PRINT: resposta do Gemini ao Prompt 6 — revisão final]

---

## Apêndice A — Mapa de prints

Use esta lista para não esquecer nenhuma captura de tela:

| # | Print | Seção |
|---|-------|-------|
| 1 | Resposta do Gemini — plano de implantação | 1.5 |
| 2 | `gh auth status` autenticado | 2.1 |
| 3 | Resposta do Gemini — organização do repositório | 2.4 |
| 4 | Árvore de pastas do repositório | 2.4 |
| 5 | Settings → Collaborators (papéis) | 3.1 |
| 6 | Settings → Code security (Dependabot/Secret scanning) | 3.2 |
| 7 | 2FA ativado na conta | 3.2 |
| 8 | Resposta do Gemini — segurança | 3.2 |
| 9 | `git log` ou aba Commits | 4.1 |
| 10 | Pull Request com checks verdes + merge | 4.2 |
| 11 | Resposta do Gemini — colaboração | 4.2 |
| 12 | Actions com CI verde | 5.1 |
| 13 | Site em produção (GitHub Pages) | 5.2 |
| 14 | Release v2.0.0 | 5.4 |
| 15 | Resposta do Gemini — CI/CD | 5.4 |
| 16 | Resposta do Gemini — revisão final | 6.4 |

## Apêndice B — Prompts do Google Gemini

Todos os prompts prontos para copiar e colar estão reunidos no arquivo
[`prompts-gemini.md`](./prompts-gemini.md). Cole o print de cada resposta no
ponto indicado acima.

---

<div align="center">
PortfolioHUB · Entrega Final · Lucca Mariz · CEUB 2026
</div>
