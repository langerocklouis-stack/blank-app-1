import streamlit as st
import pandas as pd

st.title("🎈 César est gay")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.title("Graphique en barres")
# Données exemple
data = pd.DataFrame({
    "Catégorie": ["A", "B", "C", "D", "E"],
    "Valeur": [23, 45, 56, 78, 32]
})
# Graphique en barres
st.bar_chart(data.set_index("Catégorie"))
