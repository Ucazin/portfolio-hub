# Política de Segurança — PortfolioHUB

Este documento descreve as práticas de segurança adotadas no repositório e o
canal para reportar vulnerabilidades. Ele faz parte da documentação da
**Entrega Final — Implantação do PortfolioHUB**.

---

## 1. Versões suportadas

Por ser um repositório de portfólio acadêmico, apenas a versão mais recente
publicada na branch `main` recebe correções de segurança.

| Versão | Suportada |
|--------|-----------|
| `main` (mais recente) | ✅ |
| Releases anteriores | ❌ |

---

## 2. Como reportar uma vulnerabilidade

Se você encontrar uma vulnerabilidade, **não abra uma issue pública**. Em vez disso:

1. Envie um e-mail para **luccamariz01@gmail.com** com o assunto
   `[SEGURANCA] PortfolioHUB`.
2. Descreva o problema, o impacto e, se possível, um passo a passo para reproduzir.
3. O retorno ocorre em até **5 dias úteis**.

Alternativamente, use o canal privado do GitHub:
**Security → Report a vulnerability** (GitHub Private Vulnerability Reporting),
quando habilitado.

---

## 3. Práticas de segurança aplicadas neste repositório

Estas são as boas práticas de segurança efetivamente configuradas:

### Controle de acesso
- **Autenticação de dois fatores (2FA)** obrigatória na conta do mantenedor.
- **Princípio do menor privilégio**: colaboradores recebem o menor papel
  (`role`) necessário — `Read`, `Triage`, `Write`, `Maintain` ou `Admin`.
- Acesso administrativo restrito ao dono do repositório.

### Proteção da branch principal
- **Branch protection** ativa na `main`:
  - Push direto bloqueado — alterações só via Pull Request.
  - Exige **1 aprovação** de revisão.
  - Exige **status checks** (CI) verdes antes do merge.
  - Exige **resolução de conversas**.
  - **Histórico linear** obrigatório; *force push* e deleção bloqueados.

### Higiene de segredos e dados sensíveis
- **`.gitignore` robusto** evitando o commit de `.env`, chaves, bancos locais,
  credenciais e artefatos de build.
- **Secret scanning** e **push protection** habilitados (quando disponíveis no
  plano), para impedir o envio acidental de segredos.

### Gestão de dependências
- **Dependabot alerts** habilitado para receber avisos de CVEs.
- **`dependabot.yml`** monitorando as dependências `pip` dos projetos Python e
  as *actions* do GitHub Actions.

### Integração contínua
- Pipeline de **GitHub Actions** validando a estrutura e os arquivos a cada push
  e Pull Request, evitando que código quebrado chegue à produção (GitHub Pages).

---

## 4. O que NÃO é versionado

Nunca são commitados neste repositório:

- Arquivos `.env` e variáveis de ambiente.
- Chaves de API, tokens ou credenciais.
- Bancos de dados locais (`*.sqlite`, `*.db`).
- Dados pessoais sensíveis.

---

Mantenedor: **Lucca Mariz** ([@Ucazin](https://github.com/Ucazin))
