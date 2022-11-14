# streamlit_app.py

import streamlit as st
import pandas as pd

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.header("Welcome to my amazing Website!")
st.write("This is where I will post completed projects, information about myself, and more!")

st.form('my_form_identifier')
st.form_submit_button('Submit to me')
st.container()
st.columns(spec)
col1, col2 = st.columns(2)
col1.subheader('Columnisation')
st.expander('Expander')
 with st.expander('Expand'):
   st.write('Juicy deets')
