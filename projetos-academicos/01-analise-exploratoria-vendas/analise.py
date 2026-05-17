"""
Análise Exploratória de Vendas — Projeto Acadêmico
Autor: Lucca Mariz (Ucazin)
Curso: Ciência de Dados e Machine Learning — CEUB
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "vendas.csv"


def gerar_dataset_demo(caminho: Path, n_linhas: int = 1000, seed: int = 42) -> None:
    """Gera um dataset fictício de vendas para fins de demonstração."""
    rng = np.random.default_rng(seed)
    categorias = ["Eletrônicos", "Vestuário", "Alimentos", "Livros", "Casa"]
    produtos = {
        "Eletrônicos": ["Notebook", "Smartphone", "Fone", "Tablet", "Smartwatch"],
        "Vestuário":   ["Camiseta", "Calça", "Jaqueta", "Tênis", "Boné"],
        "Alimentos":   ["Café", "Chocolate", "Biscoito", "Cereal", "Suco"],
        "Livros":      ["Romance", "Técnico", "Biografia", "Infantil", "Mangá"],
        "Casa":        ["Toalha", "Travesseiro", "Panela", "Lâmpada", "Quadro"],
    }

    datas = pd.date_range("2025-01-01", "2025-12-31", freq="D")
    linhas = []
    for _ in range(n_linhas):
        cat = rng.choice(categorias)
        prod = rng.choice(produtos[cat])
        quantidade = int(rng.integers(1, 8))
        preco_unit = round(float(rng.uniform(20, 800)), 2)
        data = rng.choice(datas)
        linhas.append({
            "data":         pd.Timestamp(data),
            "categoria":    cat,
            "produto":      prod,
            "quantidade":   quantidade,
            "preco_unit":   preco_unit,
            "receita":      round(quantidade * preco_unit, 2),
        })

    df = pd.DataFrame(linhas).sort_values("data").reset_index(drop=True)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(caminho, index=False, encoding="utf-8")
    print(f"[OK] Dataset gerado em {caminho} ({len(df)} linhas)")


def carregar_dados(caminho: Path) -> pd.DataFrame:
    if not caminho.exists():
        print("[i] Dataset não encontrado, gerando versão demonstrativa...")
        gerar_dataset_demo(caminho)
    df = pd.read_csv(caminho, parse_dates=["data"])
    return df


def resumo_estatistico(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print(" RESUMO DO DATASET")
    print("=" * 60)
    print(f"Registros: {len(df):,}")
    print(f"Período:   {df['data'].min().date()} a {df['data'].max().date()}")
    print(f"Colunas:   {list(df.columns)}\n")

    print("Estatísticas das colunas numéricas:")
    print(df[["quantidade", "preco_unit", "receita"]].describe().round(2))


def insights_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    resumo = (
        df.groupby("categoria")
          .agg(
              receita_total=("receita", "sum"),
              receita_media=("receita", "mean"),
              qtd_vendas=("receita", "count"),
          )
          .sort_values("receita_total", ascending=False)
          .round(2)
    )
    print("\n" + "=" * 60)
    print(" RECEITA POR CATEGORIA")
    print("=" * 60)
    print(resumo)
    return resumo


def top_produtos(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    top = (
        df.groupby(["categoria", "produto"])["receita"]
          .sum()
          .sort_values(ascending=False)
          .head(n)
          .round(2)
    )
    print("\n" + "=" * 60)
    print(f" TOP {n} PRODUTOS POR RECEITA")
    print("=" * 60)
    print(top)
    return top


def receita_por_mes(df: pd.DataFrame) -> pd.Series:
    serie = (
        df.assign(mes=df["data"].dt.to_period("M"))
          .groupby("mes")["receita"]
          .sum()
          .round(2)
    )
    print("\n" + "=" * 60)
    print(" RECEITA POR MÊS")
    print("=" * 60)
    print(serie)
    print(f"\nMês de maior faturamento: {serie.idxmax()} (R$ {serie.max():,.2f})")
    return serie


def plotar_graficos(df: pd.DataFrame, resumo_cat: pd.DataFrame,
                    top: pd.DataFrame, serie_mes: pd.Series) -> None:
    sns.set_theme(style="whitegrid", palette="viridis")

    # 1. Receita por categoria
    fig, ax = plt.subplots(figsize=(9, 5))
    resumo_cat["receita_total"].plot(kind="bar", ax=ax, color="#4C72B0")
    ax.set_title("Receita Total por Categoria", fontsize=14, fontweight="bold")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Receita (R$)")
    ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    plt.savefig(BASE_DIR / "grafico_01_receita_por_categoria.png", dpi=120)
    plt.close()

    # 2. Top produtos
    fig, ax = plt.subplots(figsize=(9, 5))
    top.plot(kind="barh", ax=ax, color="#55A868")
    ax.set_title("Top 5 Produtos por Receita", fontsize=14, fontweight="bold")
    ax.set_xlabel("Receita (R$)")
    ax.set_ylabel("Categoria / Produto")
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(BASE_DIR / "grafico_02_top_produtos.png", dpi=120)
    plt.close()

    # 3. Receita por mês
    fig, ax = plt.subplots(figsize=(9, 5))
    serie_mes.plot(kind="line", marker="o", ax=ax, color="#C44E52", linewidth=2)
    ax.set_title("Evolução da Receita Mensal", fontsize=14, fontweight="bold")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Receita (R$)")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(BASE_DIR / "grafico_03_receita_por_mes.png", dpi=120)
    plt.close()

    print("\n[OK] Gráficos salvos em:", BASE_DIR.resolve())


def main() -> None:
    print("\n>>> ANÁLISE EXPLORATÓRIA DE VENDAS <<<\n")
    df = carregar_dados(DATA_FILE)
    resumo_estatistico(df)
    resumo_cat = insights_por_categoria(df)
    top = top_produtos(df, n=5)
    serie_mes = receita_por_mes(df)
    plotar_graficos(df, resumo_cat, top, serie_mes)
    print("\n>>> Análise concluída com sucesso. <<<\n")


if __name__ == "__main__":
    main()
