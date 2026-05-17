"""
Classificação Iris com Machine Learning — Projeto Acadêmico
Autor: Lucca Mariz (Ucazin)
Curso: Ciência de Dados e Machine Learning — CEUB
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


BASE_DIR = Path(__file__).parent
SEED = 42


def carregar_dataset():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name="especie")
    return X, y, iris.target_names


def preparar_dados(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, stratify=y, random_state=SEED
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    return X_train_s, X_test_s, y_train, y_test


def treinar_modelos(X_train, y_train):
    modelos = {
        "KNN (k=5)":            KNeighborsClassifier(n_neighbors=5),
        "Regressão Logística":  LogisticRegression(max_iter=1000, random_state=SEED),
        "Random Forest":        RandomForestClassifier(n_estimators=100, random_state=SEED),
    }
    treinados = {}
    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        treinados[nome] = modelo
    return treinados


def avaliar(modelo, X_test, y_test, classes, nome: str):
    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n{'─' * 60}")
    print(f" {nome}  ·  Acurácia: {acc:.4f}")
    print("─" * 60)
    print(classification_report(y_test, y_pred, target_names=classes, digits=3))
    return acc, confusion_matrix(y_test, y_pred)


def plotar_matriz_confusao(cm, classes, nome, ax):
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=classes, yticklabels=classes, ax=ax, cbar=False)
    ax.set_title(f"{nome}", fontsize=11, fontweight="bold")
    ax.set_xlabel("Predito")
    ax.set_ylabel("Real")


def plotar_resultados(matrizes, classes, acuracias):
    # Grid de matrizes de confusão
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    for ax, (nome, cm) in zip(axes, matrizes.items()):
        plotar_matriz_confusao(cm, classes, nome, ax)
    fig.suptitle("Matrizes de Confusão dos Modelos", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "grafico_01_matrizes_confusao.png", dpi=120)
    plt.close()

    # Comparação de acurácia
    fig, ax = plt.subplots(figsize=(8, 4.5))
    nomes = list(acuracias.keys())
    valores = list(acuracias.values())
    cores = ["#4C72B0", "#55A868", "#C44E52"]
    bars = ax.bar(nomes, valores, color=cores)
    ax.set_ylim(0.85, 1.02)
    ax.set_ylabel("Acurácia")
    ax.set_title("Comparação de Acurácia entre Modelos", fontsize=13, fontweight="bold")
    for bar, val in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.005,
                f"{val:.3f}", ha="center", fontweight="bold")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "grafico_02_comparacao_modelos.png", dpi=120)
    plt.close()

    print("\n[OK] Gráficos salvos em:", BASE_DIR.resolve())


def main():
    print("\n>>> CLASSIFICAÇÃO IRIS COM MACHINE LEARNING <<<\n")
    X, y, classes = carregar_dataset()
    print(f"Dataset: {len(X)} amostras · {len(X.columns)} features · {len(classes)} classes")
    print(f"Classes: {list(classes)}")

    X_train, X_test, y_train, y_test = preparar_dados(X, y)
    print(f"\nTreino: {len(y_train)} amostras · Teste: {len(y_test)} amostras")

    modelos = treinar_modelos(X_train, y_train)

    acuracias = {}
    matrizes = {}
    for nome, modelo in modelos.items():
        acc, cm = avaliar(modelo, X_test, y_test, classes, nome)
        acuracias[nome] = acc
        matrizes[nome] = cm

    plotar_resultados(matrizes, classes, acuracias)

    melhor = max(acuracias, key=acuracias.get)
    print(f"\n>>> Melhor modelo: {melhor} ({acuracias[melhor]:.4f}) <<<\n")


if __name__ == "__main__":
    main()
