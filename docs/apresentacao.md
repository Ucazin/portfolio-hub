# Apresentação do Repositório — PortfolioHUB

> Documento de apresentação geral do repositório, suas seções e objetivos.
> Atende ao item **6. Revisão Final e Apresentação** do Desafio de Entrega Intermediária.

---

## 1. Quem sou eu

**Lucca Coelho Mendes de Mariz Dantas Del Bosco** — graduando em Ciência de Dados e Machine Learning no Centro Universitário de Brasília (CEUB), Campus Asa Norte.

- **GitHub:** [@Ucazin](https://github.com/Ucazin)
- **LinkedIn:** [lucca-mariz](https://www.linkedin.com/in/lucca-mariz/)
- **E-mail:** luccamariz01@gmail.com

## 2. Por que este repositório existe

O `PortfolioHUB` é meu repositório pessoal centralizado, criado para:

1. **Aplicar versionamento profissional** com Git e GitHub
2. **Demonstrar** projetos acadêmicos e pessoais publicamente
3. **Documentar** cada projeto com READMEs bem estruturados
4. **Publicar** uma vitrine viva via GitHub Pages
5. **Integrar** com o LinkedIn para reforço de perfil profissional

Atende integralmente aos 6 itens da entrega intermediária descritos no PDF do desafio.

## 3. Estrutura do repositório

```
portfolio-hub/
├── index.html                          ← Página do GitHub Pages
├── assets/                             ← CSS, JS e imagens da vitrine
├── projetos-academicos/                ← Projetos da graduação
│   ├── 01-analise-exploratoria-vendas/
│   └── 02-classificacao-iris-ml/
├── projetos-pessoais/                  ← Projetos pessoais
│   └── 03-dashboard-covid-visualizacao/
├── docs/                               ← Documentação geral
│   ├── apresentacao.md                 ← (este arquivo)
│   └── roteiro-video.md
├── README.md                           ← Documento de boas-vindas
├── LICENSE                             ← Licença MIT
└── .gitignore
```

## 4. Projetos em destaque

### 4.1 Análise Exploratória de Vendas *(acadêmico)*
Pipeline de **EDA** em Python, com Pandas e Matplotlib. Gera estatística descritiva, identifica top produtos, calcula receita por categoria e plota a evolução mensal. Demonstra fluência no fluxo básico de análise de dados.

### 4.2 Classificação Iris com Machine Learning *(acadêmico)*
Pipeline supervisionado completo com **scikit-learn**: split estratificado, normalização, treino de 3 modelos (KNN, Regressão Logística, Random Forest), avaliação por acurácia e matriz de confusão. Demonstra entendimento do ciclo de ML.

### 4.3 Dashboard COVID Interativo *(pessoal)*
Página web estática com **HTML + CSS + JavaScript puro + Chart.js**, exibindo KPIs e 3 tipos de gráficos. Demonstra capacidade de comunicar dados de forma visual e responsiva.

## 5. Decisões técnicas

| Decisão | Motivo |
|--------|--------|
| **HTML/CSS/JS vanilla** na página principal | Zero dependências, deploy instantâneo no GitHub Pages, baixa fricção |
| **Tema dark tech** | Coerente com identidade técnica e moderna |
| **Mobile-first** | Garante boa experiência em qualquer dispositivo |
| **Markdown nos READMEs** | Padrão da indústria, renderiza bem no GitHub |
| **Licença MIT** | Permite reuso educacional |
| **Tag v1.0.0** | Sinaliza release oficial da entrega intermediária |

## 6. Versionamento aplicado

Versionamento semântico (SemVer). A versão atual é `v1.0.0`, marcada com tag Git e correspondente à entrega intermediária da disciplina.

Histórico de commits segue padrão **Conventional Commits**:
- `feat:` para novas funcionalidades
- `docs:` para documentação
- `style:` para estilização
- `chore:` para configuração

## 7. Próximos passos (pós-entrega)

- Adicionar projetos das próximas disciplinas
- Implementar workflow de CI (GitHub Actions) para lint dos READMEs
- Criar tag `v1.1.0` com novos projetos
- Expandir o dashboard COVID com dados reais (open data)

---

**Última atualização:** 16 de maio de 2026
