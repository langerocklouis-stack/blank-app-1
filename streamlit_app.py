import streamlit as st
import pandas as pd


# Données exemple
data = pd.DataFrame({
    "Catégorie": ["Mao", "Candice", "Fostine"],
    "Valeur": [23, 45, 56, 78, 32]
})
# Graphique en barres
st.bar_chart(data.set_index("Catégorie"))
