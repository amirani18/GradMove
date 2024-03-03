import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import toml

from streamlit_extras.grid import grid
from cost import provider_by_state, categorize_access, generate_chart, cost, title_x, public
from access import get_score_by_state, identify_access_level, draw_gauge_chart, access

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

    def grid_one():
        random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

        # Row 1:
        my_grid.dataframe(random_df, use_container_width=True)
        my_grid.line_chart(random_df, use_container_width=True)

        # healthcare_cost func
        def healthcare_cost(option):
            # Retrieve the state abbreviation based on the selected city
            input_city = option
            input_state = city_to_state.get(input_city)

            # Integrate cost functionality
            providerCount = provider_by_state(input_state)
            access_level = categorize_access(providerCount)
            st.write(f"This state has a {access_level} number of providers:{providerCount}")
            
            # Generate cost chart
            generate_chart(input_state)
        healthcare_cost(option)

        
        # Row 2:
        my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
        my_grid.text_input("Your name")
        my_grid.button("Send", use_container_width=True)

        # healthcare_access func
        def healthcare_access(option):
            input_city = option
            input_state = city_to_state.get(input_city)

            #Integrate access functionality
            score = get_score_by_state(input_state)
            access_level = identify_access_level(score)

            draw_gauge_chart(input_state, "Clinic Accessibility")

        healthcare_access(option)

        # Row 3:
        my_grid.text_area("Your message", height=40)
        # Row 4:
        my_grid.button("Example 1", use_container_width=True)
        my_grid.button("Example 2", use_container_width=True)
        my_grid.button("Example 3", use_container_width=True)
        my_grid.button("Example 4", use_container_width=True)
        # Row 5 (uses the spec from row 1):
        with my_grid.expander("Show Filters", expanded=True):
            st.slider("Filter by Age", 0, 100, 50)
            st.slider("Filter by Height", 0.0, 2.0, 1.0)
            st.slider("Filter by Weight", 0.0, 100.0, 50.0)
        my_grid.dataframe(random_df, use_container_width=True)
    grid_one()

def page2():
    st.header("GradMove 🎓")
    st.write("This is Chatbot.")
    def example():
        random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

        # Row 1:
        my_grid.dataframe(random_df, use_container_width=True)
        my_grid.line_chart(random_df, use_container_width=True)
        # Row 2:
        my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
        my_grid.text_input("Your name")
        my_grid.button("Send", use_container_width=True)
        # Row 3:
        my_grid.text_area("Your message", height=40)
        # Row 4:
        my_grid.button("Example 1", use_container_width=True)
        my_grid.button("Example 2", use_container_width=True)
        my_grid.button("Example 3", use_container_width=True)
        my_grid.button("Example 4", use_container_width=True)
        # Row 5 (uses the spec from row 1):
        with my_grid.expander("Show Filters", expanded=True):
            st.slider("Filter by Age", 0, 100, 50)
            st.slider("Filter by Height", 0.0, 2.0, 1.0)
            st.slider("Filter by Weight", 0.0, 100.0, 50.0)
        my_grid.dataframe(random_df, use_container_width=True)
    example()

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



