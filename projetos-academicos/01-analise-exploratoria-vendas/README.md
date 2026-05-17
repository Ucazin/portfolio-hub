# Projeto 01 — Análise Exploratória de Vendas

> Projeto acadêmico desenvolvido no curso de **Ciência de Dados e Machine Learning** (CEUB).

## Objetivo

Realizar uma **Análise Exploratória de Dados (EDA)** sobre um conjunto fictício de vendas de uma rede de varejo, identificando padrões de receita, sazonalidade, performance por categoria e top produtos.

## Conceitos Aplicados

- Carregamento e inspeção de dados com **Pandas**
- Estatística descritiva (média, mediana, desvio padrão, quartis)
- Tratamento de valores ausentes e tipos de dado
- Agrupamento e agregação (`groupby`)
- Visualização com **Matplotlib** e **Seaborn**
- Geração de relatório textual com insights

## Estrutura

```
01-analise-exploratoria-vendas/
├── README.md
├── requirements.txt
├── analise.py              # Script principal
└── data/
    └── vendas.csv          # Dataset fictício (gerado pelo script)
```

## Como Executar

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Execute o script
python analise.py
```

O script irá:
1. Gerar o dataset `data/vendas.csv` (caso não exista)
2. Carregar os dados
3. Imprimir estatísticas descritivas no terminal
4. Salvar 3 gráficos PNG na própria pasta do projeto

## Resultados Esperados

Ao final da execução, você verá no terminal:
- Resumo do dataset (linhas, colunas, tipos)
- Faturamento total e médio por categoria
- Top 5 produtos por receita
- Mês com maior faturamento

E na pasta do projeto:
- `grafico_01_receita_por_categoria.png`
- `grafico_02_top_produtos.png`
- `grafico_03_receita_por_mes.png`

## Tecnologias

| Ferramenta | Versão | Função |
|-----------|--------|--------|
| Python    | 3.10+  | Linguagem base |
| Pandas    | 2.x    | Manipulação de dados |
| NumPy     | 1.x    | Operações numéricas |
| Matplotlib| 3.x    | Visualização base |
| Seaborn   | 0.13+  | Visualização estatística |

## Aprendizados

Este projeto consolida fundamentos de **EDA**, que é o primeiro passo de qualquer análise de dados séria. A leitura crítica das estatísticas descritivas e dos gráficos permite formular hipóteses que orientam a modelagem posterior.

---

**Autor:** Lucca Mariz · [GitHub](https://github.com/Ucazin) · [LinkedIn](https://www.linkedin.com/in/lucca-mariz/)
