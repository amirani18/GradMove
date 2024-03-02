import streamlit as st
import pandas as pd

# # Initial page config
title = "GradMove"
st.title(title + " 🎓")
st.write("by Areej, Shreya, Vibha, Mihika")

# user inputs on sidebar
st.sidebar.title("vibes 💖")
S = st.sidebar.slider('How Excited Are You to Be Here?', value = 1, 
                      min_value = 10, max_value = 100)
st.sidebar.write("Excitement Level", S)

# # main body
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

# Create a sidebar navigation menu
page = st.sidebar.selectbox("Select a page", ["Housing Hub", "Chatbot"])

# Depending on the selected page, show different content
if page == "Housing Hub":
    st.header("GradMove 🎓")
    st.write("Welcome to Housing Hub!")
elif page == "Chatbot":
    st.header("GradMove 🎓")
    st.write("This is Chatbot.")
# elif page == "Page 3":
#     st.header("Page 3")
#     st.write("You are on Page 3.")



