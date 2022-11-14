# streamlit_app.py

import streamlit as st
import pandas as pd

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.header('Welcome to my amazing Website!')
st.write('This is where I will post completed projects, information about myself, and more!')

st.container()
col1, col2 = st.columns(2)
with col1:
  #st.header('About Me')
  st.expander('Expander')
  with st.expander('About Me'):
    st.subheader('My Name Is Ari Davidson')
    st.write('I am currently teaching my self full-stack web development.')
with col2:
  #st.header('Projects')
  st.expander('Expander')
  with st.expander('Projects'):
    st.subheader('Currently Working On...')
    st.write('Stuffs')
    tab1, tab2 = st.tabs(["Smart Glasses","N.A"])
    tab1.subheader('Smart Glasses')
    tab2.subheader('N.A')
