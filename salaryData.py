import pandas as pd
import os

def process_city_data(city):
    # Load the combined_occupations.csv file into a DataFrame
    df = pd.read_csv('combined_occupations.csv')
    
    # Filter rows where OCC_CODE starts with '15' - Computational and Mathematical Occupations
    filtered_df = df[df['OCC_CODE'].str.startswith('15')]
    
    # Check if the input city is in the DataFrame
    if city in filtered_df['AREA_TITLE'].values:
        # Filter the DataFrame for the selected city
        city_df = filtered_df[filtered_df['AREA_TITLE'] == city]
        final_df = city_df[['AREA_TITLE', 'H_MEAN', 'A_MEAN', 'OCC_TITLE']]
        
        # Save the city DataFrame to a CSV file
        city_csv_file_name = f"{city.replace(',', '').replace(' ', '_')}_occupations.csv"
        final_df.to_csv(city_csv_file_name, index=False)
        
        print(f"Data for {city} saved to {city_csv_file_name}")
    else:
        print(f"No data available for {city}")

