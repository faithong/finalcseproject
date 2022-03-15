import streamlit as st
import pandas as pd
# import seaborn as sns

col1, col2, col3 = st.columns([3, 1, 1])
st.text("")
st.text("")
col4, col5, col6 = st.columns([3, 3, 3])


with col1:
    st.title("CSE 163 Final Project")
    st.caption("Here I will include a short description on our project.")

aa = pd.read_csv('/Users/faithong/Desktop/cse163final/cse163final/data_ea.csv')