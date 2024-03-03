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
import kaleido
from streamlit_extras.grid import grid
from cost import abs_dev, provider_by_state, categorize_access, generate_chart, cost, title_x, public
from access import baseline_access, stdev_access, get_score_by_state, identify_access_level, draw_gauge_chart, access

# Define your OpenAI API Key
secrets = toml.load(".streamlit/secrets.toml")
os.environ['OPENAI_API_KEY'] = "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"
openai_api_key = os.environ.get('OPENAI_API_KEY')


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
    "Boston, MA": "Massachusetts",
    "Los Angeles, CA": "California",

}

def page_config():
    """Configures the initial page settings."""
    # st.image("gradmove_white_logo-removebg.png", use_column_width=True)
    title = "GradMove"
    st.title(f"{title} 🎓")
    st.subheader("Embark on Your Next Chapter with Confidence.")
    st.write("by Areej, Shreya, Vibha, Mihika")
    st.markdown(
    """
    <p style='color: #desd83; font-family: verdana, sans-serif;'>GradMove is here to streamline your transition from college to career. As you prepare to start your first job in a new city, we understand the whirlwind of questions and decisions you face. Where will you live? How will you commute? What healthcare options are available? GradMove is your dedicated companion, designed to fast-forward through the initial, overwhelming searches and present you with clear, concise, and crucial information about your future home.</p>
    """,
    unsafe_allow_html=True
)
    st.sidebar.title("Vibes 💖")

def user_inputs():
    """Handles user inputs in the sidebar and displays chat responses."""
    st.sidebar.image('gradmovebig.png', use_column_width=True)
    excitement_level = st.sidebar.slider('How Excited Are You to Be Here?', 1, 10, 100)
    st.sidebar.write("Excitement Level", excitement_level)
    chat_input = st.sidebar.text_input("Ask me anything:")
    st.sidebar.write("Chatbot disabled :((")
    if chat_input:
        response = handle_chat_input(chat_input, use_langchain=False)  # Adjust use_langchain based on your setup
        st.sidebar.write("Response:", response)

def handle_chat_input(user_input, use_langchain=False):
    """Handles the chat input, querying OpenAI or LangChain."""
    # openai_api_key = os.environ['OPENAI_API_KEY']
    openai.api_key = openai_api_key
    # Directly using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        api_key=openai_api_key
    )
    return response.choices[0].message.content
    
def main_body():
    st.markdown('---')
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

    @st.cache_data
    def fetch_variable():
        time.sleep(5)  # Simulating a delay
        return True

    with st.spinner('Fetching variable...'):
        variable = fetch_variable()

    st.write('Fetched variable:', variable)
    
    st.write('Fetching data for:', option)
    st.write("Excited to move to", option, "and start your new job?")
    st.write("Let's get started!")

    st.markdown('---')

    def info_in_cols():
        # Create columns
        col1, col2 = st.columns(2)

        # Display different information in each column
        with col1:
            st.subheader("Healthcare Cost 💸")
            # healthcare_cost func
            def healthcare_cost(option):
                # Retrieve the state abbreviation based on the selected city
                input_city = option
                input_state = city_to_state.get(input_city)
                
                # Generate cost chart
                st.write("Abortion costs dependant on location.")
                generate_chart(input_state)
            healthcare_cost(option)

        with col2:
            st.subheader("Healthcare Access 🔓")
            # healthcare_access func
            def healthcare_access(option):
                input_city = option
                input_state = city_to_state.get(input_city)

                #Integrate access functionality
                score = get_score_by_state(input_state)
                color = identify_access_level(score)

                # paragraph explaining stats
                st.write(f"{score} % of counties in this state have no clinics.")

                # display
                image_path = draw_gauge_chart(score)
                st.image(image_path)
            healthcare_access(option)

    info_in_cols()

    def healthcare_info_in_cols():
        # Create columns
        col1, col2 = st.columns(2)

        # Display different information in each column
        with col1:
            st.text("Healthcare Links 🔗")
            def create_button(url, button_text):
                button_html = f"""
                    <a href="{url}" target="_blank">
                    <button style="
                    background: linear-gradient(to right, #ff758c 0%, #ff7eb3 100%);
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 20px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border: none;
                    border-radius: 12px;
                    ">
                    {button_text}
                    </button>
                    </a>
                    """
                # Render the button in Streamlit
                st.markdown(button_html, unsafe_allow_html=True)
            create_button("https://abortionfunds.org/find-a-fund/", "Need a fund?")

        with col2:
            st.text("Healthcare Clinics 🏥")
            # healthcare_access func
            def create_button(url, button_text):
                button_html = f"""
                    <a href="{url}" target="_blank">
                    <button style="
                    background: linear-gradient(to right, #ff758c 0%, #ff7eb3 100%);
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 20px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border: none;
                    border-radius: 12px;
                    ">
                    {button_text}
                    </button>
                    </a>
                    """
                # Render the button in Streamlit
                st.markdown(button_html, unsafe_allow_html=True)
        
            create_button("https://www.abortionfinder.org", "Need a clinic?")

    healthcare_info_in_cols()
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
    centered_scaled_svg_content = f'''<div style="text-align: center;">
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

def main():
    """Main function to orchestrate the Streamlit app."""
    if st.session_state.get('history') is None:
        st.session_state.history = []
    
    page_config()
    user_inputs()  # Now includes displaying the response in the sidebar
    main_body()

if __name__ == "__main__":
    main()
