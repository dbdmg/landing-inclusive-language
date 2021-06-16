import streamlit as st

"""
# 👋 Ciao!

Benvenuto al Tool di annotazione per il Linguaggio Inclusivo.
"""

"""
## 📄 Converti il tuo **.docx** in un **.csv**
"""

st.file_uploader("Carica un documento Word dal tuo PC")

"""
## 🖋️ Annota il tuo CSV

Se hai già convertito il tuo documento in CSV vai al tool di annotazione dal pulsante in
basso. Lì, ti sarà possibile caricare il tuo file e potrai annotare le frasi per 
il Linguaggio Inclusivo. 

"""

st.button("Vai al tool di annotazione")

"""
## 🤝 Unisci il tuo **.csv** in un documento Word.
"""

st.file_uploader("Carica un documento CSV dal tuo PC")
