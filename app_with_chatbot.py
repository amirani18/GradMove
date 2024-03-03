import streamlit as st
import pandas as pd
import openai
import langchain
import toml
import housingDataFunction
import matplotlib.pyplot as plt
from salaryData import process_city_data
from transit import get_walk_score_selenium
import os
import time

# Define your OpenAI API Key
secrets = toml.load(".streamlit/secrets.toml")

OPENAI_API_KEY = "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"

# how do I enter the api key in the secrets.toml file?
# [openai]
# api_key =

# Load the config settings from config.toml
config = toml.load('.streamlit/config.toml')
# Get the theme settings
theme_settings = config.get('theme', {})
base_theme = theme_settings.get('base', 'dark')
primary_color = theme_settings.get('primaryColor', '#8A9A5B')
background_color = theme_settings.get('backgroundColor', '#000000')
secondary_background_color = theme_settings.get('secondaryBackgroundColor', '#f0f2f6')
text_color = theme_settings.get('textColor', '#e0218a')
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
        'cities': ["San Francisco, CA", "Chicago, IL", "New York, NY", "Seattle, WA", "Cambridge, MA", "Boston, MA", "Los Angeles, CA", "Austin, TX", "Denver, CO", "Portland, OR", "Atlanta, GA", "Dallas, TX", "Philadelphia, PA", "Kansas City, MO"]
    })
    
    option = st.selectbox(
        'Which city do you plan to move to?',
        df['cities']
    )
    
    # st.write('You chose:', option)
    @st.cache_data
    def fetch_variable():
        time.sleep(5)  # Simulating a delay
        return True

    with st.spinner('Fetching variable...'):
        variable = fetch_variable()

    st.write('Fetched variable:', option)
    # @st.cache_data
    # def fetch_variable():
    #     time.sleep(5)  # Simulating a delay
    #     return option

    # with st.spinner('Fetching data...'):
    #     variable = fetch_variable()

    st.write('Found:', variable)
    st.write("Excited to move to", option, "and start your new job?")
    st.write("Let's get started!")

    st.markdown('---')

    option2 = ""

    #one to one hot encoding of cities
    if option == "San Francisco, CA":
        option2 = "San Francisco-Oakland-Hayward, CA"

    elif option == "Chicago, IL":
        option2 = "Chicago-Naperville-Elgin, IL-IN-WI"

    elif option == "New York, NY":
        option2 = "New York-Newark-Jersey City, NY-NJ-PA"

    elif option == "Seattle, WA":
        option2 = "Seattle-Tacoma-Bellevue, WA"

    elif option == "Cambridge, MA":
        option2 = "Boston-Cambridge-Newton, MA-NH"

    elif option == "Atlanta, GA":
        option2 = "Atlanta-Sandy Springs-Roswell, GA"

    elif option == "Dallas, TX":
        option2 = "Dallas-Fort Worth-Arlington, TX"
    
    elif option == "Kansas City, MO":
        option2 = "Kansas City, MO-KS"
    
    elif option == "Philadelphia, PA":  
        option2 = "Philadelphia-Camden-Wilmington, PA-NJ-DE-MD"

    elif option == "Denver, CO":
        option2 = "Denver-Aurora-Lakewood, CO"
    
    elif option == "Boston, MA":
        option2 = "Boston-Cambridge-Newton, MA-NH"
    
    elif option == "Portland, OR":
        option2 = "Portland-Vancouver-Hillsboro, OR-WA"

    elif option == "Los Angeles, CA":
        option2 = "Los Angeles-Long Beach-Anaheim, CA"

    elif option == "Austin, TX":
        option2 = "Austin-Round Rock, TX"

    


    
    st.subheader("Rent in " + option + " over the years")
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

    st.markdown('---')
    #add space before this element
    st.write('\n')  # Add a new line for spacing
    st.subheader("Appartments to rent nearby")
    #get_walk_score_selenium(city, state_code)
    get_walk_score_selenium(option.split(",")[0], option.split(",")[1].strip())
    appt_for_rent_image = f"{option.split(',')[0].replace(' ', '_')}_appts_to_rent.png"
    st.image(appt_for_rent_image)

    

    st.markdown('---')
    # salary by occupation 
    if option2 != "":
        process_city_data(option2)
        city_csv_file_name = f"{option2.replace(',', '').replace(' ', '_')}_occupations.csv"

        if os.path.exists(city_csv_file_name):
        # Load the CSV file
            df = pd.read_csv(city_csv_file_name)
            # change the column names
            df.columns = ['Area', 'Hourly Mean Wage', 'Annual Mean Wage', 'Occupation']
        
        # Display the DataFrame in the app
            st.subheader(f"Salary Data for {option}:")
            st.dataframe(df)
        else:
        # If the file doesn't exist, inform the user
            st.write(f"Salary data for {option} is not available. Check back soon!")


    #walkability 
    st.markdown('---')
    st.subheader(f"Walkability for {option}")
    #get_walk_score_selenium(option.split(",")[0], option.split(",")[1].strip())
    walk_score_image = f"{option.split(',')[0].replace(' ', '_')}_walk_score2.svg"

    #appt_for_rent_image = f"{option.split(',')[0].replace(' ', '_')}_appts_to_rent.png"

    col1, col2 = st.columns([1, 3])

    #st.image(walk_score_image)
    with open(walk_score_image, 'r', encoding='utf-8') as file:
        svg_content = file.read()
    centered_scaled_svg_content = f'''
<div style="text-align: center;">
    <div style="width: 100%; display: inline-block;">{svg_content}</div>
</div>
'''
    with col1:
        # Center the image
        st.markdown(centered_scaled_svg_content, unsafe_allow_html=True)
    with col2:
        #read from file called walkability_data.txt
        with open("walkability_data.txt", "r") as file:
            ret_walkability_data = file.read()  
        st.write(ret_walkability_data)
    


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
