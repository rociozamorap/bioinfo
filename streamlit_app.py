import streamlit as st
import py3Dmol
import requests

import copy
import json

import streamlit as st
from streamlit_image_select import image_select

from utils import (
    st_get_osm_geometries,
    st_plot_all,
    get_colors_from_style,
    gdf_to_bytesio_geojson,
)
from prettymapp.geo import GeoCodingError, get_aoi
from prettymapp.settings import STYLES

st.set_page_config(
    page_title="prettymapp", page_icon="🖼️", initial_sidebar_state="collapsed"
)
st.markdown("# Prettymapp")
