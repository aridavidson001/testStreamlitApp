# streamlit_app.py

import streamlit as st
import pandas as pd

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.header("Welcome to my amazing Website!")
st.write("This is where I will post completed projects, information about myself, and more!")

st.container()
col1, col2 = st.columns(2)
col1.header("About Me")
col1.expander("Click to learn more")

col2.header("Projects")
col1.expander("Click to learn more")

st.expander('Expander')
with st.expander('Expand'):
   st.write('Juicy deets')
