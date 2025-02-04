import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Chargement du fichier Excel
try:
    df = pd.read_excel("KPI_CGO_SelfBar.xlsx")
    st.write("Fichier chargé avec succès !")
    st.write("Colonnes disponibles :", df.columns)

    # Corrige les noms de colonnes (supprime les espaces indésirables)
    df.columns = df.columns.str.strip()

    # Vérifie la présence des colonnes nécessaires
    required_columns = ["KPI", "Réalisation", "Objectif"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        st.error(f"Colonnes manquantes : {', '.join(missing_columns)}")
    else:
        # Corrige les types des colonnes
        df["Objectif"] = pd.to_numeric(df["Objectif"], errors="coerce")
        df["Réalisation"] = pd.to_numeric(df["Réalisation"], errors="coerce")
        df["KPI"] = df["KPI"].astype(str)

        # Gère les valeurs NaN
        df = df.dropna(subset=["Objectif", "Réalisation"])

        # Génère le graphique
        fig, ax = plt.subplots()
        ax.barh(df["KPI"], df["Objectif"], color="lightgray", label="Objectif")
        ax.barh(df["KPI"], df["Réalisation"], color="blue", label="Réalisation")
        ax.set_xlabel("Valeurs")
        ax.set_ylabel("KPI")
        ax.legend()
        st.pyplot(fig)
except FileNotFoundError:
    st.error("Le fichier Excel 'KPI_CGO_SelfBar.xlsx' est introuvable.")
except Exception as e:
    st.error(f"Erreur inattendue : {e}")
