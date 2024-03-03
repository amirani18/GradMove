import streamlit as st
import pandas as pd
import openai
import langchain

# Define your OpenAI API Key
OPENAI_API_KEY = "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"  # For production, use st.secrets to manage your API key securely

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
    
    if use_langchain:
        # Using LangChain wrapper
        lc_response = adapters.lc_openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model you prefer
            messages=[{"role": "user", "content": user_input}],
            api_key=openai_api_key
        )
        return lc_response["choices"][0]["message"]["content"]
    else:
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
