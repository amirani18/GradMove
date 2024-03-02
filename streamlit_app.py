import streamlit as st
from pathlib import Path
import pandas as pd
import base64

# Initial page config
title = "GradMove"
st.title(title + " 🎓")
st.write("by Areej, Shreya, Vibha, Mihika")
st.sidebar.title("Options")

# user inputs on sidebar
S = st.sidebar.slider('How Excited Are You to Be Here?', value = 1, 
                      min_value = 0, max_value = 10)
st.sidebar.write("Excitement Level", S)

# main body
st.header("Are you a fresh grad who's landed your dream job? Are you struggling to find your next home? Introducing: GradMove!")
st.markdown("Your go-to app for finding housing near your dream job, curated based on tastes in housing, price, transport, and access to healthcare.")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 90, 30, 92]
})

option = st.selectbox(
    'Which city do you plan to move to?',
    df['first column']
)

'You selected: ', option

