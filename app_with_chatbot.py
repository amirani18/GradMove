import streamlit as st
import pandas as pd
import openai
import langchain
import toml

# Define your OpenAI API Key
secrets = toml.load(".streamlit/secrets.toml")

OPENAI_API_KEY = secrets['openai']['api_key']

# Load the config settings from config.toml
config = toml.load('config.toml')

# Get the theme settings
theme_settings = config.get('theme', {})

base_theme = theme_settings.get('base', 'light')
primary_color = theme_settings.get('primaryColor', '#8A9A5B')
background_color = theme_settings.get('backgroundColor', '#ffffff')
secondary_background_color = theme_settings.get('secondaryBackgroundColor', '#f0f2f6')
text_color = theme_settings.get('textColor', '#F4C2C2')
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
        'cities': ["San Francisco", "Chicago", "New York", "Seattle", "Cambridge", "Amsterdam"],
    })
    
    option = st.selectbox(
        'Which city do you plan to move to?',
        df['cities']
    )
    
    st.write('You selected:', option)

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
