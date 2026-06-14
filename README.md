<div align="center">

# PortfolioHUB

### Repositório de projetos acadêmicos e pessoais

**Lucca Mariz** — Ciência de Dados e Machine Learning
Centro Universitário de Brasília (CEUB) — Campus Asa Norte

[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Online-2ea44f?style=for-the-badge&logo=github)](https://ucazin.github.io/portfolio-hub/)
[![Versão](https://img.shields.io/badge/versão-1.0.0-blue?style=for-the-badge)](https://github.com/Ucazin/portfolio-hub/releases)
[![Licença](https://img.shields.io/badge/licença-MIT-yellow?style=for-the-badge)](LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/lucca-mariz/)

</div>

---

## Sobre

Este repositório reúne meus projetos acadêmicos e pessoais desenvolvidos ao longo da graduação em **Ciência de Dados e Machine Learning** no CEUB. O objetivo é construir um portfólio público versionado que demonstre, na prática, conhecimentos em análise de dados, modelagem estatística, aprendizado de máquina e desenvolvimento web.

Cada projeto contém sua própria documentação (`README.md`), seu código-fonte e, quando aplicável, datasets e visualizações.

## Estrutura do Repositório

```
portfolio-hub/
├── index.html                          # Página principal (GitHub Pages)
├── assets/                             # Recursos da página (CSS, JS, imagens)
│   ├── css/
│   ├── js/
│   └── img/
├── projetos-academicos/                # Projetos da graduação
│   ├── 01-analise-exploratoria-vendas/
│   └── 02-classificacao-iris-ml/
├── projetos-pessoais/                  # Projetos pessoais
│   └── 03-dashboard-covid-visualizacao/
├── slides/                             # Apresentação interativa em HTML
│   ├── index.html
│   └── slides.css
├── docs/                               # Documentação geral
│   ├── apresentacao.md
│   └── roteiro-video.md
├── README.md                           # Este arquivo
├── LICENSE
└── .gitignore
```

### Apresentação interativa

Veja a apresentação completa do repositório em formato slides navegáveis:

**[`ucazin.github.io/portfolio-hub/slides/`](https://ucazin.github.io/portfolio-hub/slides/)**

## Projetos em Destaque

### Acadêmicos

| Projeto | Descrição | Tecnologias |
|---------|-----------|-------------|
| [Análise Exploratória de Vendas](./projetos-academicos/01-analise-exploratoria-vendas/) | EDA completa de um dataset de vendas, com estatística descritiva e visualizações. | Python, Pandas, Matplotlib |
| [Classificação Iris com ML](./projetos-academicos/02-classificacao-iris-ml/) | Modelo de classificação supervisionada usando o dataset clássico Iris. | Python, scikit-learn, NumPy |

### Pessoais

| Projeto | Descrição | Tecnologias |
|---------|-----------|-------------|
| [Dashboard COVID Interativo](./projetos-pessoais/03-dashboard-covid-visualizacao/) | Visualização de dados de COVID-19 em página web interativa. | HTML, CSS, JavaScript, Chart.js |

## Tecnologias Utilizadas

- **Linguagens:** Python, JavaScript, HTML, CSS
- **Bibliotecas de Dados:** Pandas, NumPy, Matplotlib, Seaborn, scikit-learn
- **Visualização Web:** Chart.js
- **Versionamento:** Git, GitHub
- **Publicação:** GitHub Pages
- **Documentação:** Markdown

## Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/Ucazin/portfolio-hub.git
cd portfolio-hub

# Para os projetos Python (dentro da pasta de cada projeto)
pip install -r requirements.txt
python nome-do-script.py

# Para a página web (index.html), basta abrir no navegador
# ou usar um servidor local:
python -m http.server 8000
# Acesse http://localhost:8000
```

## Versionamento

Este repositório segue versionamento semântico ([SemVer](https://semver.org/lang/pt-BR/)). A versão atual é **v1.0.0**, marcando a entrega intermediária da disciplina.

Veja o histórico completo em [Releases](https://github.com/Ucazin/portfolio-hub/releases).

## Governança, Colaboração e Segurança

Este repositório segue boas práticas de governança e segurança, aplicadas na
**Entrega Final — Implantação em Produção**:

- **Fluxo de colaboração:** toda mudança passa por *branch* + *Pull Request* com
  revisão obrigatória. Veja [`CONTRIBUTING.md`](CONTRIBUTING.md).
- **Branch principal protegida:** push direto bloqueado, exige review e testes verdes.
- **Integração contínua:** [GitHub Actions](.github/workflows/ci.yml) valida
  estrutura e HTML a cada push e Pull Request.
- **Segurança:** 2FA, branch protection, Dependabot e secret scanning. Política em
  [`SECURITY.md`](SECURITY.md).
- **Revisores definidos:** [`CODEOWNERS`](.github/CODEOWNERS).
- **Código de conduta:** [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

📄 A documentação completa da implantação está em
[`docs/implantacao/`](docs/implantacao/DOCUMENTO-IMPLANTACAO.md).

## Contato

- **Nome:** Lucca Coelho Mendes de Mariz Dantas Del Bosco
- **E-mail:** luccamariz01@gmail.com
- **GitHub:** [@Ucazin](https://github.com/Ucazin)
- **LinkedIn:** [Lucca Mariz](https://www.linkedin.com/in/lucca-mariz/)

## Licença

Distribuído sob a Licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.

---

<div align="center">
Feito com dedicação por <strong>Lucca Mariz</strong> · CEUB 2026
</div>
