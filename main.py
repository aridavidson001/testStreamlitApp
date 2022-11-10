import streamlit as st
import pandas as pd
import plotly.express as px
st.header('Test for Importing and Exporting Data to and from Google Sheets')
data = pd.read_csv("https://docs.google.com/spreadsheets/d/1RPBl2AuY5UVqp_ay8huKWGYNlIfRM2Zb6KbK2I28xrs/gviz/tq?tqx=out:csv.csv")
df = pd.DataFrame(data)

st.dataframe(df) 

teamNumber = st.number_input('Team Number')
st.write(teamNumber)

autoPoints = st.number_input('Points during Auto:')
st.write(autoPoints)
