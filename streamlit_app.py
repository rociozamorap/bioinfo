import streamlit as st
import py3Dmol
import requests
from stmol import showmol
import json

def get_protein_info(prot):
    req = requests.get(f'https://data.rcsb.org/rest/v1/core/entry/{prot}/')
    prot_data = json.loads(req.text)
    title = prot_data["struct"]["title"]
    descriptor = prot_data["struct"]["pdbx_descriptor"]
    return descriptor, title

st.sidebar.title('Show Proteins')
protein = st.sidebar.text_input('Ingrese la secuencia de ADN:', "")
