# Projeto 03 — Dashboard COVID Interativo

> Projeto pessoal desenvolvido para praticar **visualização de dados na web**.

## Objetivo

Construir um **dashboard web interativo** que apresenta indicadores fictícios de COVID-19 (casos, óbitos e recuperados) ao longo do tempo, demonstrando habilidades em visualização de dados na web sem dependência de back-end.

A página é 100% estática — pode ser hospedada gratuitamente no GitHub Pages, Vercel, Netlify ou qualquer servidor de arquivos.

## Conceitos Aplicados

- Estruturação semântica com **HTML5**
- Estilização responsiva com **CSS3** (Grid, Flexbox, variáveis CSS)
- Gráficos interativos com **Chart.js** (linha, barras, doughnut)
- Manipulação do DOM com **JavaScript** puro
- Tema escuro com paleta consistente
- Design **mobile-first**

## Estrutura

```
03-dashboard-covid-visualizacao/
├── README.md
├── index.html        # Página principal
├── styles.css        # Estilização
├── script.js         # Lógica e gráficos
└── data.js           # Dados fictícios separados
```

## Como Executar

Não há dependências para instalar. Basta:

```bash
# Abra direto no navegador:
# Clique duas vezes em index.html

# Ou sirva localmente para evitar restrições de CORS:
python -m http.server 8000
# Acesse http://localhost:8000
```

## Funcionalidades

- 4 cartões com indicadores principais (Total de casos, Óbitos, Recuperados, Ativos)
- Gráfico de linha mostrando a evolução temporal de casos
- Gráfico de barras comparando estados/regiões
- Gráfico de doughnut com distribuição percentual
- Filtros por período (não funcional na demo, ilustrativo do design)
- Responsivo para desktop, tablet e mobile

## Tecnologias

| Ferramenta | Função |
|-----------|--------|
| HTML5     | Estrutura semântica |
| CSS3      | Layout e tema escuro |
| JavaScript (ES6+) | Lógica e interatividade |
| Chart.js v4 | Renderização dos gráficos |

> **Nota:** Os dados utilizados são **fictícios** e servem apenas para fins de demonstração visual. Não devem ser interpretados como informações reais sobre a pandemia.

## Aprendizados

A capacidade de **comunicar dados visualmente** é tão importante quanto a capacidade de processá-los. Bibliotecas como Chart.js, D3.js e Plotly são ferramentas essenciais para o cientista de dados que precisa entregar dashboards e relatórios consumíveis por stakeholders não-técnicos.

---

**Autor:** Lucca Mariz · [GitHub](https://github.com/Ucazin) · [LinkedIn](https://www.linkedin.com/in/lucca-mariz/)
