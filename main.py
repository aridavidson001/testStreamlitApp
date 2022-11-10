# streamlit_app.py

import streamlit as st
from gsheetsdb import connect
import pandas as pd
# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]

st.header('Test for Importing and Exporting Data to and from Google Sheets')
data = pd.read_csv("sheet_url")

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
