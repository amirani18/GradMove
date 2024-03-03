import streamlit as st
import pandas as pd

import openai
import langchain
# from langchain import openai as adapters  # If using LangChain

# Initial page config
title = "GradMove"
st.title(title + " 🎓")
st.write("by Areej, Shreya, Vibha, Mihika")
st.sidebar.title("vibes 💖")

# user inputs on sidebar
S = st.sidebar.slider('How Excited Are You to Be Here?', value = 1, 
                      min_value = 10, max_value = 100)
st.sidebar.write("Excitement Level", S)
# main body
st.header("Are you a fresh grad who's landed your dream job in a brand new city?")
st.subheader("Introducing: GradMove!")
st.markdown("Your go-to app for finding housing near your dream job, curated based on tastes in housing, price, transport, and access to healthcare.")

# selectbox for cities

df = pd.DataFrame({
    'cities': ["San Francisco", "Chicago", "New York", "Seattle", "Cambridge", "Amsterdam" ],
})

option = st.selectbox(
    'Which city do you plan to move to?',
    df['cities']
)

'You selected: ', option

OPENAI_API_KEY = ""


def handle_chat_input(user_input, use_langchain=False):
    openai_api_key = OPENAI_API_KEY
    openai.api_key = openai_api_key
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        api_key=openai_api_key
    )
    return response.choices[0].message.content


chat_input = st.text_input("Ask me anything:")
if chat_input:
    response = handle_chat_input(chat_input, use_langchain=False)  # Set use_langchain based on your preference
    st.write(response)


