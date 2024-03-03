import streamlit as st
import pandas as pd
import matplotlib
import toml

from cost import provider_by_state, categorize_access, generate_chart, cost, title_x, public

# # Initial page config
title = "GradMove"
st.title(title + " 🎓")
st.write("by Areej, Shreya, Vibha, Mihika")

# Load the config settings from config.toml
config = toml.load('.streamlit/config.toml')

# Get the theme settings
theme_settings = config.get('theme', {})

base_theme = theme_settings.get('base', 'dark')
primary_color = theme_settings.get('primaryColor', '#8A9A5B')
background_color = theme_settings.get('backgroundColor', '#ffffff')
secondary_background_color = theme_settings.get('secondaryBackgroundColor', '#f0f2f6')
text_color = theme_settings.get('textColor', '#F4C2C2')
font = theme_settings.get('font', 'serif')

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

city_to_state = {
    "San Francisco, CA": "California",
    "Atlanta, GA": "Georgia",
    "Chicago, IL": "Illinois",
    "Seattle, WA": "Washington",
    "Denver, CO": "Colorado",
    "Kansas City, KS": "Kansas",
    "New York, NY": "New York",
    "Austin, TX": "Texas",
    "Philadelphia, PA": "Pennsylvania",
    "Cambridge, MA": "Massachusetts",

}

def page1():
    st.header("GradMove 🎓")
    st.write("Welcome to Housing Hub!")

    # selectbox for cities
    df = pd.DataFrame(
        {
            "cities": [
                "San Francisco, CA",
                "Atlanta, GA",
                "Chicago, IL",
                "Seattle, WA",
                "Denver, CO",
                "Kansas City, KS",
                "New York, NY",
                "Austin, TX",
                "Philadelphia, PA",
                "Cambridge, MA",
            ]
        }
    )
  
    option = st.selectbox(
        'Which city do you plan to move to?',
        df['cities']
    )

    'You selected: ', option

    def healthcare_cost(option):
        # Retrieve the state abbreviation based on the selected city
        input_city = option
        input_state = city_to_state.get(input_city)

        # Integrate cost functionality
        providerCount = provider_by_state(input_state)
        access_level = categorize_access(providerCount)
        st.write(f"This state has a {access_level} number of providers:{providerCount}")

        # Generate cost chart
        chart = generate_chart(input_state)
        # Create two columns
        col1, col2 = st.columns(2)

        # Display an image in the first column
        with col1:
            st.subheader('Image in Column 1')

        # Display a different image in the second column
        with col2:
            st.subheader('Image in Column 2')
            st.image(chart, caption='cost of providers in state')

    healthcare_cost(option)

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



