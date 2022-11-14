# streamlit_app.py

import streamlit as st
import pandas as pd

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.header("Welcome to my amazing Website!")
st.write("This is where I will post completed projects, information about myself, and more!")

st.container()
col1, col2 = st.columns(2)
with col1:
  st.header("About Me")
  st.expander('Expander')
  with st.expander('Expand'):
    st.write('Expanded ')

col2.header("Projects")
 # col2.expander("Click to learn more")
  # with col2.expander('Expand'):
   #   st.write('Expanded ')

st.expander('Expander')
with st.expander('Expand'):
   st.write('Expanded ')
