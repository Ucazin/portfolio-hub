# 🎬 Roteiro DEFINITIVO do Vídeo — Entrega Final (Implantação) · ~5 min

> Vídeo para o **YouTube** (visibilidade **Não listado**). Cobre as **6 seções**
> da Entrega Final na ordem: GitHub → Segurança → Colaboração → Produção → Gemini.
>
> **Título sugerido:** `PortfolioHUB — Implantação em Produção + IA Gemini · Lucca Mariz · CEUB 2026`
>
> **Como usar:** o texto em "🎙️ FALE" é pra ler em voz alta. O texto em
> "🖥️ TELA" diz o que deixar na tela naquele momento. É só seguir de cima a baixo.

---

## Antes de apertar REC

- [ ] **Abas abertas nesta ordem:** (1) home do repo · (2) Settings → Branches ·
      (3) Settings → conta (2FA) · (4) PR #1 · (5) Actions · (6) site no ar ·
      (7) Gemini com as conversas
- [ ] Fonte do navegador aumentada (**Ctrl +**)
- [ ] Notificações desativadas, abas pessoais fechadas
- [ ] Áudio testado (grave 10s e ouça)
- [ ] Pode gravar **em partes e cortar** — não precisa sair perfeito de primeira

---

## Bloco 1 · Abertura — 0:00 a 0:20

🖥️ **TELA:** sua câmera (se quiser) ou a home do repositório.

🎙️ **FALE:**
> "Oi! Eu sou o Lucca Mariz, aluno de Ciência de Dados e Machine Learning no CEUB.
> Neste vídeo eu apresento a entrega final do meu portfólio: a **implantação em
> produção** do PortfolioHUB no GitHub. Vou mostrar a organização do repositório,
> a segurança, o fluxo de colaboração, o site no ar e como usei o **Google Gemini**
> como apoio em cada etapa."

---

## Bloco 2 · O Repositório *(Seções 1 e 2)* — 0:20 a 1:00

🖥️ **TELA:** home do repositório (`github.com/Ucazin/portfolio-hub`), rolando as pastas.

🎙️ **FALE:**
> "Este é o repositório. Ele está organizado por finalidade: a pasta
> `projetos-academicos` com os trabalhos da graduação, `projetos-pessoais` com os
> meus projetos, `docs` com toda a documentação, e a pasta `.github`, que guarda a
> automação e a governança.
>
> Eu adicionei arquivos que todo repositório profissional tem: o **README**, o
> **CONTRIBUTING** com as regras de contribuição, o **SECURITY** com a política de
> segurança, um **código de conduta**, o **CODEOWNERS** e templates de issue e de
> pull request. Repara, aqui no painel lateral, que o GitHub marca o perfil de
> comunidade como completo."

🖥️ *Passe o mouse pelos arquivos `CONTRIBUTING.md`, `SECURITY.md` e pela pasta `.github`.*

---

## Bloco 3 · Segurança: proteção da branch *(Seção 3)* — 1:00 a 1:30

🖥️ **TELA:** **Settings → Branches** → clique na **regra de proteção da `main`** pra abrir os detalhes.

🎙️ **FALE:**
> "Na segurança, a branch principal, a `main`, está **protegida**. Ninguém faz envio
> direto nela. Toda mudança precisa passar por um **pull request**, com **revisão
> obrigatória** e com os **testes automáticos verdes** antes de poder entrar. Também
> exijo histórico linear e bloqueio o force-push. Na prática, isso impede que
> qualquer coisa quebrada ou não revisada chegue ao site."

🖥️ *Mostre as caixas marcadas: require pull request, require approvals, require status checks, require linear history.*

---

## Bloco 4 · Segurança: 2FA e dependências *(Seção 3)* — 1:30 a 1:50

🖥️ **TELA:** página de **2FA** da sua conta (Settings da conta → Password and authentication). **Não mostre os códigos de recuperação.**

🎙️ **FALE:**
> "Além disso, ativei a **autenticação de dois fatores** na minha conta, então nem
> com a senha alguém entra sem o segundo fator. E deixei o **Dependabot** e o
> **secret scanning** ligados: um monitora as dependências e avisa sobre falhas de
> segurança, o outro impede o envio acidental de senhas ou chaves no código."

---

## Bloco 5 · Colaboração: o Pull Request *(Seção 4)* — 1:50 a 2:15

🖥️ **TELA:** **Pull Request #1** (`/pull/1`), mostrando o selo roxo **"Merged"** e, rolando, os checks verdes.

🎙️ **FALE:**
> "Toda essa implantação foi feita pelo fluxo profissional de colaboração. Eu não
> escrevi nada direto na `main`: criei uma **branch separada**, abri este **pull
> request**, os testes rodaram automaticamente, e só depois de tudo verde e
> revisado eu fiz o **merge**. Aqui está o pull request já integrado. É assim que se
> trabalha em equipe sem bagunçar o código principal."

---

## Bloco 6 · Testes / Integração Contínua *(Seção 5)* — 2:15 a 2:35

🖥️ **TELA:** aba **Actions**, mostrando as execuções com ✅ verde.

🎙️ **FALE:**
> "Esses testes vêm do **GitHub Actions**. A cada push e a cada pull request, ele
> roda dois jobs: um valida a **estrutura** do repositório e o outro valida os
> **arquivos HTML**. Aqui dá pra ver tudo passando em segundos. É a minha rede de
> segurança antes de qualquer coisa ir pra produção."

---

## Bloco 7 · 🌐 PRODUÇÃO: o site no ar *(Seção 5)* — 2:35 a 3:05  ← ÁPICE

🖥️ **TELA:** o site publicado — `https://ucazin.github.io/portfolio-hub/`. Role um pouco mostrando as seções; redimensione a janela pra mostrar que é responsivo.

🎙️ **FALE:**
> "E aqui está o resultado: o portfólio **no ar**, em produção, no **GitHub Pages**.
> Esse é o ambiente de produção do projeto, e ele republica **automaticamente** a
> cada merge na `main`. O site é responsivo, então funciona bem no computador e no
> celular. Tudo que eu mostrei até agora — organização, segurança e testes — existe
> pra garantir que **essa página** esteja sempre estável e funcionando."

🖥️ *Diminua a largura da janela pra simular o celular e mostre o layout se adaptando.*

---

## Bloco 8 · Release de produção *(Seções 5 e 6)* — 3:05 a 3:15

🖥️ **TELA:** a página da **Release v2.0.0**.

🎙️ **FALE:**
> "Marquei essa entrada em produção com a versão **2.0.0**, seguindo versionamento
> semântico: a `1.0.0` foi a entrega anterior, e a `2.0.0` é a implantação."

---

## Bloco 9 · O Google Gemini *(requisito da IA — apoia todas as seções)* — 3:15 a 4:00

🖥️ **TELA:** o **Gemini**, rolando pelas conversas. Fale uma frase por conversa.

🎙️ **FALE:**
> "Em cada etapa eu usei o **Google Gemini** como apoio. Eu fiz seis consultas a ele:"

| Mostrando a conversa de... | 🎙️ FALE |
|---|---|
| Plano | "Primeiro pedi um **plano de implantação** completo, que usei como checklist." |
| Organização | "Perguntei a **melhor forma de organizar as pastas** e a governança." |
| Segurança | "Consultei as **boas práticas de segurança** — proteção de branch, 2FA, Dependabot." |
| Colaboração | "Pedi pra ele explicar o **fluxo de pull requests** e por que é melhor que push direto." |
| CI/CD | "Perguntei sobre **integração contínua** e como preparar pra produção." |
| Revisão | "E no fim pedi pra ele **revisar tudo** e apontar se faltava alguma boa prática." |

🎙️ **FALE (fechando o bloco):**
> "O Gemini funcionou como um segundo par de olhos: validou meu plano e me ajudou a
> não esquecer nada importante."

> 💡 **Se quiser encurtar:** mostre com calma só **3 conversas** (plano, segurança e
> revisão) e diga "também consultei sobre organização, colaboração e CI".

---

## Bloco 10 · Encerramento — 4:00 a 4:30

🖥️ **TELA:** a home do repositório.

🎙️ **FALE:**
> "Então é isso: o PortfolioHUB está organizado, seguro, com colaboração via pull
> request, testes automáticos e publicado em produção, na versão 2.0.0 — tudo
> planejado com o apoio do Google Gemini. O projeto está aberto, com licença MIT, em
> **github.com/Ucazin/portfolio-hub**. Muito obrigado por assistir!"

---

## Mapa: cada bloco cobre qual seção

| Bloco | Tela | Seção da entrega |
|-------|------|------------------|
| 1 | Abertura | — |
| 2 | Repositório | 1 e 2 |
| 3 | Branch protection | 3 |
| 4 | 2FA + Dependabot | 3 |
| 5 | Pull Request #1 | 4 |
| 6 | Actions (CI) | 5 |
| 7 | **Site no ar** | 5 (produção) |
| 8 | Release v2.0.0 | 5 e 6 |
| 9 | Gemini | requisito IA |
| 10 | Encerramento | 6 |

✅ As 6 seções são cobertas. Nada fica faltando.

---

## Depois de gravar

- [ ] Vídeo dentro de ~5 minutos
- [ ] Subido no YouTube como **Não listado**
- [ ] Título e descrição com os links (repo, site, release)
- [ ] **Colar o link do YouTube** no documento de implantação (§6.2 e §6.3)
