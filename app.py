import streamlit as st
from src.utils import convert_doc_csv, convert_csv_doc

"""
# 👋 Ciao!

Benvenuto al Tool di annotazione per il Linguaggio Inclusivo.
"""

"""
## 📄 Converti il tuo **.docx** in un **.csv**
"""

file = st.file_uploader("Carica un documento Word dal tuo PC", type=["doc", "docx"])
if file:
    with st.spinner("Stiamo convertendo il tuo file..."):
        csv = convert_doc_csv(file)


"""
## 🖋️ Annota il tuo CSV

Se hai già convertito il tuo documento in CSV vai al tool di annotazione dal pulsante in
basso. Lì, ti sarà possibile caricare il tuo file e potrai annotare le frasi per 
il Linguaggio Inclusivo. 

"""

if st.button("Vai al tool di annotazione"):
    st.write("TODO: indirizza a Label Studio")

"""
## 🤝 Unisci il tuo **.csv** in un documento Word **.docx**
"""

file = st.file_uploader("Carica un documento CSV dal tuo PC", type=["csv"])
if file:
    with st.spinner("Stiamo creando il tuo documento..."):
        doc = convert_csv_doc(file)
