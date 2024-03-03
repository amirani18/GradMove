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

# # Create a sidebar navigation menu
# page = st.sidebar.selectbox("Select a page", ["Housing Hub", "Chatbot"])

# # Depending on the selected page, show different content
# if page == "Housing Hub":
#     st.header("GradMove 🎓")
#     st.write("Welcome to Housing Hub!")
# elif page == "Chatbot":
#     st.header("GradMove 🎓")
#     st.write("This is Chatbot.")
# # elif page == "Page 3":
# #     st.header("Page 3")
# #     st.write("You are on Page 3.")

# Define different page content
def page1():
    st.header("GradMove 🎓")
    st.write("Welcome to Housing Hub!")
    # selectbox for cities
    df = pd.DataFrame({
        'cities': ["San Francisco", "Chicago", "New York", "Seattle", "Cambridge", "Amsterdam" ],
    })

    option = st.selectbox(
        'Which city do you plan to move to?',
        df['cities']
    )

    'You selected: ', option

def page2():
    st.header("GradMove 🎓")
    st.write("This is Chatbot.")

# def page3():
#     st.header("Page 3")
#     st.write("You are on Page 3.")

# Create a simple sidebar navigation menu to switch between pages
page = st.sidebar.selectbox("Select a page", ["Housing Hub", "Chatbot"])

# Display the content of the selected page
if page == "Housing Hub":
    page1()
elif page == "Chatbot":
    page2()
# elif page == "Page 3":
#     page3()



