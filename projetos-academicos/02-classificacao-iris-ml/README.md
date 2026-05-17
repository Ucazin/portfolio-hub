# Projeto 02 — Classificação Iris com Machine Learning

> Projeto acadêmico desenvolvido no curso de **Ciência de Dados e Machine Learning** (CEUB).

## Objetivo

Construir um modelo de **classificação supervisionada** capaz de prever a espécie de uma flor Iris (Setosa, Versicolor ou Virginica) com base em quatro medidas morfológicas: comprimento e largura de pétala e sépala.

O dataset Iris é o "Hello World" do aprendizado de máquina — pequeno, balanceado, didático — e por isso ideal para demonstrar o fluxo completo de um pipeline supervisionado.

## Conceitos Aplicados

- Carregamento de dataset com **scikit-learn**
- **Divisão treino/teste** com estratificação
- Normalização de features com **StandardScaler**
- Treinamento e comparação de **3 modelos**:
  - K-Nearest Neighbors (KNN)
  - Regressão Logística
  - Random Forest
- Avaliação por **acurácia**, **matriz de confusão** e **classification report**
- Visualização da matriz de confusão

## Estrutura

```
02-classificacao-iris-ml/
├── README.md
├── requirements.txt
└── classificacao.py        # Pipeline completo
```

## Como Executar

```bash
pip install -r requirements.txt
python classificacao.py
```

O script irá:
1. Carregar o dataset Iris (vem incluído no scikit-learn)
2. Dividir em treino (70%) e teste (30%) com estratificação
3. Treinar 3 modelos diferentes
4. Imprimir métricas de avaliação no terminal
5. Salvar gráficos de matriz de confusão e comparação de modelos

## Resultados Esperados

| Modelo              | Acurácia esperada |
|---------------------|-------------------|
| KNN (k=5)           | ~95–97%           |
| Regressão Logística | ~95–97%           |
| Random Forest       | ~95–100%          |

Todos os modelos têm boa performance neste dataset, pois ele é linearmente quase separável. A diferença prática vem da estabilidade e da interpretabilidade.

## Tecnologias

| Ferramenta    | Versão | Função |
|---------------|--------|--------|
| Python        | 3.10+  | Linguagem base |
| scikit-learn  | 1.3+   | Modelos de ML e métricas |
| NumPy         | 1.x    | Operações numéricas |
| Pandas        | 2.x    | Manipulação de resultados |
| Matplotlib    | 3.x    | Visualização |
| Seaborn       | 0.13+  | Heatmaps |

## Aprendizados

Este projeto demonstra o **fluxo padrão** de um problema supervisionado:

```
Dados → Split → Preprocessamento → Modelo → Avaliação → Comparação
```

Compreender este pipeline é fundamental antes de avançar para datasets reais (sujos, desbalanceados, com features categóricas) e modelos mais complexos (redes neurais, ensembles avançados).

---

**Autor:** Lucca Mariz · [GitHub](https://github.com/Ucazin) · [LinkedIn](https://www.linkedin.com/in/lucca-mariz/)
