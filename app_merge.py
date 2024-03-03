import streamlit as st
import pandas as pd
import openai
import langchain
import toml
import housingDataFunction
import matplotlib.pyplot as plt

import housingDataFunction
import matplotlib.pyplot as plt


# Define your OpenAI API Key
secrets = toml.load(".streamlit/secrets.toml")

OPENAI_API_KEY = secrets['openai']['api_key']

# how do I enter the api key in the secrets.toml file?
# [openai]
# api_key =

# Load the config settings from config.toml
config = toml.load('.streamlit/config.toml')
# Get the theme settings
theme_settings = config.get('theme', {})
base_theme = theme_settings.get('base', 'light')
primary_color = theme_settings.get('primaryColor', '#AA336A')
background_color = theme_settings.get('backgroundColor', '#000000')
secondary_background_color = theme_settings.get('secondaryBackgroundColor', '#f0f2f6')
text_color = theme_settings.get('textColor', '#AA336A')
font = theme_settings.get('font', 'serif')

def page_config():
    """Configures the initial page settings."""
    title = "GradMove"
    st.title(f"{title} 🎓")
    st.write("by Areej, Shreya, Vibha, Mihika")
    st.sidebar.title("Vibes 💖")

def user_inputs():
    """Handles user inputs in the sidebar and displays chat responses."""
    excitement_level = st.sidebar.slider('How Excited Are You to Be Here?', 1, 10, 100)
    st.sidebar.write("Excitement Level", excitement_level)
    chat_input = st.sidebar.text_input("Ask me anything:")
    if chat_input:
        response = handle_chat_input(chat_input, use_langchain=False)  # Adjust use_langchain based on your setup
        st.sidebar.write("Response:", response)

def main_body():
    """Displays the main content of the application."""
    st.header("Are you a fresh grad who's landed your dream job in a brand new city?")
    st.subheader("Introducing: GradMove!")
    st.markdown("Your go-to app for finding housing near your dream job, curated based on tastes in housing, price, transport, and access to healthcare.")
    
    df = pd.DataFrame({
        # add all the cities in the United States
        'cities': ["San Francisco", "Chicago", "New York", "Seattle", "Cambridge", "Boston", "Los Angeles", "Austin", "Denver", "Portland", "Atlanta", "Dallas", "Philadelphia", "Kansas City",
                   "Houston", "San Antonio", "Philadelphia", "Phoenix", "Las Vegas", "San Diego", 
                   "Dallas", "Austin", "San Jose", "Jacksonville", "Indianapolis", "Charlotte",
                   "Louisville", "Sacramento",'Baltimore'],
    })
    
    option = st.selectbox(
        'Which city do you plan to move to?',
        df['cities']
    )
    
    st.write('You selected:', option)
    st.write("Excited to move to", option, "and start your new job?")
    st.write("Let's get started!")

    st.subheader("Median Rent Prices for 1-Bedroom Apartments")
    # housingDataFunction.py has the function to plot the median 
    # rent prices for 1-bedroom apartments through the years
    for city in ['Atlanta-Sandy Springs-Roswell', 'Dallas-Fort Worth-Arlington', 'Chicago-Naperville-Elgin', 'New York-Newark-Jersey City', 'Kansas City', 
          'Philadelphia-Camden-Wilmington', 'Denver-Aurora-Lakewood', 'Seattle-Tacoma-Bellevue', 'Boston-Cambridge-Newton', 'San Francisco-Oakland-Hayward']:
        if (option.split(","))[0] in city:
            st.write(city)
            
            img = housingDataFunction.plot_housing_prices_for_city(city)
            # display png image that it saves
            for j in img:
                st.image(j)
            break

    

def handle_chat_input(user_input, use_langchain=False):
    """Handles the chat input, querying OpenAI or LangChain."""
    openai_api_key = OPENAI_API_KEY
    openai.api_key = openai_api_key
    # Directly using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        api_key=openai_api_key
    )
    return response.choices[0].message.content

def main():
    """Main function to orchestrate the Streamlit app."""
    if st.session_state.get('history') is None:
        st.session_state.history = []
    
    page_config()
    user_inputs()  # Now includes displaying the response in the sidebar
    main_body()

if __name__ == "__main__":
    main()
