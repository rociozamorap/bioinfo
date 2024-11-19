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
bcolor = st.sidebar.color_picker('Pick A Color', '#DBDEDB')
protein = st.sidebar.text_input('Enter protein:', "")
style = st.sidebar.selectbox('style',['stick','line','cross','sphere','cartoon','clicksphere'])
spin = st.sidebar.checkbox('Spin', value = False)
if protein != "":
    st.sidebar.markdown(f'**{get_protein_info(protein)[0]}**')
    st.sidebar.markdown(f'**{get_protein_info(protein)[1]}**')
    xyzview = py3Dmol.view(query='pdb:'+protein)
    xyzview.setStyle({style:{'color':'spectrum'}})
    xyzview.setBackgroundColor(bcolor)
    if spin:
        xyzview.spin(True)
    else:
        xyzview.spin(False)
    xyzview.zoomTo()
    showmol(xyzview,height=500,width=800)
