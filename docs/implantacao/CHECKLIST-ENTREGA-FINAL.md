# Checklist — Entrega Final (Implantação PortfolioHUB + IA Gemini)

> ✅ = pronto (feito pelo Claude) · ⬜ = depende de você
> Data: 14/06/2026

---

## ✅ Já está pronto (configurado/criado automaticamente)

### Infraestrutura e governança (arquivos)
- [x] `CONTRIBUTING.md` — guia de contribuição e fluxo de PR
- [x] `SECURITY.md` — política de segurança
- [x] `CODE_OF_CONDUCT.md` — código de conduta
- [x] `.github/CODEOWNERS` — revisor obrigatório (@Ucazin)
- [x] `.github/pull_request_template.md` — template de PR
- [x] `.github/ISSUE_TEMPLATE/` — templates de bug e feature + config
- [x] `.github/dependabot.yml` — atualização automática de dependências
- [x] `.github/workflows/ci.yml` — pipeline de CI (2 jobs de teste)

### Documentação da entrega
- [x] `docs/implantacao/DOCUMENTO-IMPLANTACAO.md` — documento das 6 seções (vira o PDF)
- [x] `docs/implantacao/prompts-gemini.md` — 6 prompts prontos para o Gemini
- [x] `docs/implantacao/roteiro-video-final.md` — roteiro do vídeo (5 min)
- [x] `docs/implantacao/CHECKLIST-ENTREGA-FINAL.md` — este arquivo

### Configurações aplicadas no GitHub (via gh CLI)
- [x] Branch protection na `main` (PR + review + status checks + histórico linear)
- [x] Dependabot alerts ativado
- [x] Ajustes de merge (squash, deletar branch ao mergear)
- [x] Pull Request real criado e mergeado (fluxo de colaboração demonstrado)
- [x] Release `v2.0.0` publicada
- [x] README atualizado com seção de governança e segurança

---

## ⬜ Só você pode finalizar (ações manuais e pessoais)

### Na interface do GitHub (cliques)
- [ ] **Ativar 2FA** na sua conta (se ainda não estiver):
      Settings da conta → Password and authentication → Two-factor authentication.
      👉 Tire o print depois (Seção 3.2 do documento).
- [ ] **Verificar Secret scanning + Push protection**:
      Settings do repo → Code security → habilitar se aparecer desligado.
      (Em repo público costuma ser gratuito; se o botão não aparecer, anote no documento.)
- [ ] (Opcional) **Convidar um colaborador de demonstração** para evidenciar a
      gestão de usuários — comando pronto na Seção 3.1 do documento.

### Com o Google Gemini (obrigatório p/ requisito da IA)
- [ ] Fazer os **6 prompts** do arquivo `prompts-gemini.md`.
- [ ] Tirar **print de cada resposta**.
- [ ] Colar os prints nos pontos `[📷 COLAR PRINT]` do documento.

### Conteúdo pessoal no documento (campos `[PREENCHER]`)
- [x] ~~Link do Pull Request~~ — **já preenchido** (PR #1)
- [x] ~~Link da Release v2.0.0~~ — **já preenchido**
- [ ] Link do vídeo no YouTube (Seções 6.2 e 6.3)
- [ ] Conclusão/aprendizados pessoais (Seção 6.4)
- [ ] Comentários de “como usei a resposta do Gemini” (Seção 1.5)

### Vídeo
- [ ] Gravar o vídeo de 5 min seguindo `roteiro-video-final.md`
- [ ] Publicar no YouTube como **Não listado**
- [ ] Copiar o link para o documento

### Exportar e enviar
- [ ] Abrir `DOCUMENTO-IMPLANTACAO.md` (com os prints colados) e **exportar como PDF**
      (VS Code + extensão "Markdown PDF", ou colar no Google Docs e baixar PDF).
- [ ] Conferir o `Apêndice A — Mapa de prints` (16 prints) antes de exportar.
- [ ] Enviar o PDF no canal da disciplina (AVA/Moodle do CEUB).

---

## Resumo

| Bloco | Quem faz | Status |
|-------|----------|--------|
| Arquivos de governança e CI | Claude | ✅ |
| Documento das 6 seções | Claude | ✅ |
| Config de segurança via CLI | Claude | ✅ |
| PR + Release | Claude | ✅ |
| 2FA + prints do Gemini | Você | ⬜ |
| Preencher links e conclusão | Você | ⬜ |
| Gravar e subir vídeo | Você | ⬜ |
| Exportar PDF e enviar | Você | ⬜ |
