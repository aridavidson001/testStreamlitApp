import streamlit as st
import pandas as pd

st.header('Test for Importing and Exporting Data to and from Google Sheets')
data = pd.read_csv('public_gsheets_url')

df = pd.DataFrame(data)
st.dataframe(df) 

teamNumber = st.number_input('Team Number')
st.write(teamNumber)

sampleData1 = st.number_input(key = 1, label = 'Sample Data 1:')
st.write(sampleData1)

sampleData2 = st.number_input(key = 2, label = 'Sample Data 2:')
st.write(sampleData2)

sampleData3 = st.number_input(key = 3, label = 'Sample Data 3:')
st.write(sampleData3)

