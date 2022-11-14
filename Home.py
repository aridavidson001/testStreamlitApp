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
  st.expander('Expander')
  with st.expander('About Me'):
    st.subheader('My Name Is Ari Davidson')
    st.write('I am currently teaching my self full-stack web development.')
with col2:
  st.expander('Expander')
  with st.expander('Projects'):
    st.subheader('Currently Working On...')
    tab1, tab2 = st.tabs(["Smart Glasses","N.A"])
    with tab1:
      st.subheader('Smart Glasses')
      st.write('''Featuring a Raspberry Pi 0W and a 128x64 px monochrome OLED display''')
    with tab2:
      st.subheader('N.A')
      st.write('N.A.')
