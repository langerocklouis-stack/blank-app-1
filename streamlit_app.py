import streamlit as st
import pandas as pd

st.title("🎈 César est gay")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.title("Soeurs de oscar")
# Données exemple
data = pd.DataFrame({
    "Catégorie": ["Mao", "Candice", "Fostine"],
    "Valeur": [23, 45, 56, 78, 32]
})
# Graphique en barres
st.bar_chart(data.set_index("Catégorie"))
