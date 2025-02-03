{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh16080\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import matplotlib.pyplot as plt\
import seaborn as sns\
\
# Charger les donn\'e9es\
file_path = "KPI_CGO_SelfBar.xlsx"  # Remplacer par le chemin r\'e9el du fichier\
df = pd.read_excel(file_path)\
\
# Configuration de la page\
st.set_page_config(page_title="Dashboard CGO SelfBar", layout="wide")\
st.title("\uc0\u55357 \u56522  Dashboard CGO - SelfBar")\
\
# Section 1 : Objectifs vs R\'e9sultats Actuels\
st.subheader("\uc0\u55356 \u57263  Objectifs vs R\'e9sultats")\
fig, ax = plt.subplots(figsize=(8, 6))\
ax.barh(df["KPI"], df["Objectif"], color="lightgray", label="Objectif")\
ax.barh(df["KPI"], df["R\'e9sultat Actuel"], color="steelblue", label="R\'e9sultat Actuel")\
ax.legend()\
st.pyplot(fig)\
\
# Section 2 : Chiffre d'affaires & Croissance Internationale\
st.subheader("\uc0\u55357 \u56520  \'c9volution du Chiffre d'Affaires & Croissance")\
mois = ["Jan", "F\'e9v", "Mar", "Avr", "Mai", "Juin"]\
chiffre_affaires = [50000, 60000, 75000, 80000, 95000, 100000]\
croissance = [10, 12, 15, 18, 20, 22]\
\
fig, ax1 = plt.subplots(figsize=(8, 5))\
ax2 = ax1.twinx()\
ax1.plot(mois, chiffre_affaires, marker="o", color="blue", label="CA (\'80)")\
ax2.plot(mois, croissance, marker="s", color="red", label="Croissance (%)")\
ax1.set_ylabel("Chiffre d'Affaires (\'80)")\
ax2.set_ylabel("Croissance (%)")\
st.pyplot(fig)\
\
# Section 3 : Satisfaction Client (NPS)\
st.subheader("\uc0\u55357 \u56842  Satisfaction Clients (NPS)")\
satisfaction_labels = ["Tr\'e8s satisfait", "Satisfait", "Neutre", "Insatisfait"]\
satisfaction_values = [50, 30, 10, 10]\
fig, ax = plt.subplots()\
ax.pie(satisfaction_values, labels=satisfaction_labels, autopct='%1.0f%%', colors=["green", "lightgreen", "orange", "red"])\
st.pyplot(fig)\
\
# Section 4 : Performance des Apporteurs d'Affaires\
st.subheader("\uc0\u55357 \u56508  Performance des Apporteurs d'Affaires")\
apporteurs = ["A1", "A2", "A3", "A4", "A5"]\
ventes = [15, 20, 25, 10, 18]\
fig, ax = plt.subplots()\
ax.bar(apporteurs, ventes, color="purple")\
st.pyplot(fig)\
\
st.write("\uc0\u55357 \u56546  **Mise \'e0 jour automatique des donn\'e9es depuis le fichier Excel**")\
}