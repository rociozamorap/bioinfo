import streamlit as st
import py3Dmol
import requests
import json



def get_protein_info(prot):
    req = requests.get(f'https://data.rcsb.org/rest/v1/core/entry/{prot}/')
    prot_data = json.loads(req.text)
    title = prot_data["struct"]["title"]
    descriptor = prot_data["struct"]["pdbx_descriptor"]
    return descriptor, title

st.sidebar.title('Proteinas')
protein = st.sidebar.text_input('Ingrese la secuencia de ADN:', "")



st.set_page_config(
    page_title="prettymapp", page_icon="🖼️", initial_sidebar_state="collapsed"
)
st.markdown("# Prettymapp")

with open("./streamlit-prettymapp/examples.json", "r", encoding="utf8") as f:
    EXAMPLES = json.load(f)

if not st.session_state:
    st.session_state.update(EXAMPLES["Macau"])

    lc_class_colors = get_colors_from_style("Peach")
    st.session_state.lc_classes = list(lc_class_colors.keys())  # type: ignore
    st.session_state.update(lc_class_colors)
    st.session_state["previous_style"] = "Peach"
    st.session_state["previous_example_index"] = 0

example_image_pattern = "streamlit-prettymapp/example_prints/{}_small.png"
example_image_fp = [
    example_image_pattern.format(name.lower()) for name in list(EXAMPLES.keys())[:4]
]
index_selected = image_select(
    "",
    images=example_image_fp,
    captions=list(EXAMPLES.keys())[:4],
    index=0,
    return_value="index",
)
