import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Chargement du fichier Excel
try:
    df = pd.read_excel("KPI_CGO_SelfBar.xlsx")
    st.write("Fichier chargé avec succès !")
    st.write(df.dtypes)  # Vérifie les types des colonnes
    st.write(df.head())  # Affiche les premières lignes pour diagnostic
except FileNotFoundError:
    st.error("Le fichier Excel 'KPI_CGO_SelfBar.xlsx' est introuvable. Assure-toi qu'il est bien dans le même dossier que ce script.")
except Exception as e:
    st.error(f"Erreur inattendue lors du chargement : {e}")

# Tracer le graphique uniquement si df est chargé
if 'df' in locals():
    # Vérifier et corriger les colonnes nécessaires
    df["Objectif"] = pd.to_numeric(df["Objectif"], errors="coerce")
    df["KPI"] = df["KPI"].astype(str)
    df = df.dropna(subset=["Objectif"])

    # Création du graphique
    fig, ax = plt.subplots()
    ax.barh(df["KPI"], df["Objectif"], color="lightgray", label="Objectif")
    ax.barh(df["KPI"], df["Réalisation"], color="blue", label="Résultat Actuel")
    ax.set_xlabel("Valeurs")
    ax.set_ylabel("KPI")
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("Impossible de générer le graphique, le DataFrame est vide.")
