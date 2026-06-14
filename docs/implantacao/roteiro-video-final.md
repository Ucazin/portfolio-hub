# Roteiro do Vídeo — Entrega Final (Implantação) · 5 minutos

> Vídeo a ser publicado no **YouTube** (visibilidade **Não listado**) para a
> Entrega Final. Foco: **a implantação em produção, a segurança e a colaboração**
> — diferente do vídeo da intermediária, que apresentava os projetos.
>
> **Título sugerido:** `PortfolioHUB — Implantação em Produção + IA Gemini · Lucca Mariz · CEUB 2026`

---

## Configuração da gravação

- **Duração-alvo:** 5 minutos (não passar disso).
- **Resolução:** 1080p · **Áudio:** microfone limpo, sem ruído.
- **Telas para deixar abertas antes de gravar:**
  1. Repositório no GitHub (`github.com/Ucazin/portfolio-hub`)
  2. Aba **Settings → Branches** (branch protection)
  3. Aba **Actions** (CI verde)
  4. O **Pull Request** da implantação
  5. O site em produção (`ucazin.github.io/portfolio-hub`)
  6. Uma conversa do **Gemini** aberta
- **Software:** OBS Studio, Loom ou ScreenRec.
- Desative notificações e feche abas pessoais.

---

## Roteiro em blocos

### Bloco 1 · Abertura (0:00 – 0:30)

**Mostrar:** sua câmera ou a home do repositório.

> "Oi, eu sou o Lucca Mariz, aluno de Ciência de Dados e Machine Learning no CEUB.
> Neste vídeo apresento a **Entrega Final** do meu portfólio: a **implantação em
> produção** do PortfolioHUB no GitHub, com foco em organização, segurança e
> colaboração — e mostro como usei o **Google Gemini** como apoio em cada etapa."

---

### Bloco 2 · Planejamento com o Gemini (0:30 – 1:15)

**Mostrar:** a conversa do Gemini com o plano de implantação.

> "Antes de começar, planejei a implantação com a ajuda do Google Gemini. Pedi um
> plano profissional cobrindo organização do repositório, gestão de usuários,
> segurança, colaboração e publicação. A partir dessas respostas, montei meu
> checklist de execução."

*Role a resposta do Gemini rapidamente.*

---

### Bloco 3 · Configuração e organização (1:15 – 2:10)

**Mostrar:** a árvore de pastas do repositório no GitHub.

> "O repositório está organizado por finalidade: projetos acadêmicos, projetos
> pessoais, documentação e a pasta `.github` com toda a governança e a automação.
> Adicionei arquivos profissionais: CONTRIBUTING, SECURITY, CODE_OF_CONDUCT,
> CODEOWNERS e templates de issue e de Pull Request."

*Abra a pasta `.github` e mostre os arquivos.*

---

### Bloco 4 · Segurança e gestão de usuários (2:10 – 3:10)

**Mostrar:** Settings → Branches (proteção) e Settings → Code security.

> "Na segurança, apliquei várias boas práticas. A branch `main` está **protegida**:
> ninguém faz push direto — tudo passa por Pull Request com revisão obrigatória e
> testes verdes. Ativei a **autenticação de dois fatores**, o **Dependabot** para
> alertas de dependências e o **secret scanning** para impedir o envio acidental
> de segredos. Na gestão de usuários, sigo o **princípio do menor privilégio**:
> cada colaborador recebe só o papel necessário — Read, Write, Maintain ou Admin."

*Mostre a tela de branch protection com as regras marcadas.*

---

### Bloco 5 · Colaboração, CI e produção (3:10 – 4:30)

**Mostrar:** o Pull Request com checks verdes, depois a aba Actions, depois o site.

> "Toda a implantação foi feita pelo fluxo profissional de colaboração: criei uma
> branch, abri um **Pull Request**, o **GitHub Actions** rodou os testes
> automaticamente validando a estrutura e o HTML, e só depois mergeei na main.
>
> O ambiente de **produção** é o GitHub Pages, que faz deploy automático a cada
> merge. Aqui está o portfólio no ar, funcionando."

*Mostre o PR verde → a Action verde → o site em produção carregando.*

---

### Bloco 6 · Release e encerramento (4:30 – 5:00)

**Mostrar:** a Release `v2.0.0` e a home do repositório.

> "Marquei essa implantação com a release **v2.0.0**, sinalizando a entrada em
> produção. O projeto está aberto, documentado e seguro, em
> **github.com/Ucazin/portfolio-hub**. O Google Gemini foi essencial para validar
> cada decisão. Obrigado por assistir!"

---

## Checklist antes de gravar

- [ ] Branch protection visível em Settings → Branches
- [ ] Actions com CI verde
- [ ] Pull Request da implantação aberto numa aba
- [ ] Site em produção abrindo
- [ ] Conversa do Gemini aberta
- [ ] Notificações desativadas, abas pessoais fechadas
- [ ] Áudio testado (grave 10s e ouça)

## Checklist depois de gravar

- [ ] Vídeo dentro de 5 minutos
- [ ] Subido no YouTube como **Não listado**
- [ ] Título e descrição com links (repo, Pages, release)
- [ ] Link copiado para o documento de implantação (Seção 6.3)
