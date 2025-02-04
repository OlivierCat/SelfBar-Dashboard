import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Inspecter les types et le contenu des colonnes
st.write(df.dtypes)
st.write(df)

# Corriger les types des colonnes
df["Objectif"] = pd.to_numeric(df["Objectif"], errors="coerce")
df["KPI"] = df["KPI"].astype(str)

# Gérer les valeurs NaN
df = df.dropna(subset=["Objectif"])

# Tracer le graphique
fig, ax = plt.subplots()
ax.barh(df["KPI"], df["Objectif"], color="lightgray", label="Objectif")
ax.barh(df["KPI"], df["Réalisation"], color="blue", label="Réalisation")
ax.set_xlabel("Valeurs")
ax.set_ylabel("KPI")
ax.legend()
st.pyplot(fig)

# Charger les données
file_path = "KPI_CGO_SelfBar.xlsx"  # Remplacer par le chemin réel du fichier
df = pd.read_excel(file_path)

# Configuration de la page
st.set_page_config(page_title="Dashboard CGO SelfBar", layout="wide")
st.title("📊 Dashboard CGO - SelfBar")

# Section 1 : Objectifs vs Résultats Actuels
st.subheader("🎯 Objectifs vs Résultats")
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(df["KPI"], df["Objectif"], color="lightgray", label="Objectif")
ax.barh(df["KPI"], df["Résultat Actuel"], color="steelblue", label="Résultat Actuel")
ax.legend()
st.pyplot(fig)

# Section 2 : Chiffre d'affaires & Croissance Internationale
st.subheader("📈 Évolution du Chiffre d'Affaires & Croissance")
mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"]
chiffre_affaires = [50000, 60000, 75000, 80000, 95000, 100000]
croissance = [10, 12, 15, 18, 20, 22]

fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
ax1.plot(mois, chiffre_affaires, marker="o", color="blue", label="CA (€)")
ax2.plot(mois, croissance, marker="s", color="red", label="Croissance (%)")
ax1.set_ylabel("Chiffre d'Affaires (€)")
ax2.set_ylabel("Croissance (%)")
st.pyplot(fig)

# Section 3 : Satisfaction Client (NPS)
st.subheader("😊 Satisfaction Clients (NPS)")
satisfaction_labels = ["Très satisfait", "Satisfait", "Neutre", "Insatisfait"]
satisfaction_values = [50, 30, 10, 10]
fig, ax = plt.subplots()
ax.pie(satisfaction_values, labels=satisfaction_labels, autopct='%1.0f%%', colors=["green", "lightgreen", "orange", "red"])
st.pyplot(fig)

# Section 4 : Performance des Apporteurs d'Affaires
st.subheader("💼 Performance des Apporteurs d'Affaires")
apporteurs = ["A1", "A2", "A3", "A4", "A5"]
ventes = [15, 20, 25, 10, 18]
fig, ax = plt.subplots()
ax.bar(apporteurs, ventes, color="purple")
st.pyplot(fig)

st.write("📢 **Mise à jour automatique des données depuis le fichier Excel**")
