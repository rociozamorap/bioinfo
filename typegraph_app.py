import streamlit as st
from stmol import showmol
import py3Dmol
import requests

from rdkit import Chem
from rdkit.Chem import AllChem

def get_inchi(compound_name):
    base_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/property/InChI/TXT"
    response = requests.get(base_url)
    if response.status_code == 200:
        inchi = response.text
        return inchi
    else:
        print("Request failed with status code {}".format(response.status_code))
        return None

def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol)
    return mblock

def render_mol(xyz, inchi):
    st.sidebar.markdown(f'**InChI identifier:**')
    st.sidebar.markdown(inchi)
    xyzview = py3Dmol.view()
    xyzview.addModel(xyz,'mol')
    xyzview.setStyle({style:{'color':'spectrum'}})
    xyzview.setBackgroundColor(bcolor)
    if spin:
        xyzview.spin(True)
    else:
        xyzview.spin(False)
    xyzview.zoomTo()
    showmol(xyzview,height=500,width=800)

st.sidebar.title('Visualize chemical structure:')
compound_smiles=st.sidebar.text_input('Enter name here','')
bcolor = st.sidebar.color_picker('Pick A Color', '#DBDEDB')
style = st.sidebar.selectbox('style',['stick','sphere'])
spin = st.sidebar.checkbox('Spin', value = False)


if compound_smiles != '':
    inchi = get_inchi(compound_smiles)
    if inchi:
        smiles = Chem.MolToSmiles(Chem.MolFromInchi(inchi))
        blk=makeblock(smiles)
        render_mol(blk, inchi)
else:
    pass
