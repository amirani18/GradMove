import streamlit as st
from pathlib import Path
import pandas as pd
import base64

# Initial page config

st.set_page_config(
    page_title = 'GradMove',
    layout = "wide",
    initial_sidebar_state = "expanded",
)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 90, 30, 92]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option

