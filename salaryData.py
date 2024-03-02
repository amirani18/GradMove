import pandas as pd
import os

# Load the Excel file
df = pd.read_excel('MSA_M2022_dl.xlsx')

# Filter rows where OCC_CODE starts with '15' - Computational and Mathematical Occupations
filtered_df = df[df['OCC_CODE'].str.startswith('15')]

# List of cities you're interested in
cities = ['Atlanta-Sandy Springs-Roswell, GA', 'Dallas-Fort Worth-Arlington, TX', 'Chicago-Naperville-Elgin, IL-IN-WI', 'New York-Newark-Jersey City, NY-NJ-PA', 'Kansas City, MO-KS', 
          'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD', 'Denver-Aurora-Lakewood, CO', 'Seattle-Tacoma-Bellevue, WA', 'Boston-Cambridge-Nashua, MA-NH', 'San Francisco-Oakland-Hayward, CA']

# Initialize a list to store data for all cities
all_cities_data = []

# Loop through each city, filter the DataFrame, and append to the list
for city in cities:
    city_df = filtered_df[filtered_df['AREA_TITLE'] == city]
    final_df = city_df[['AREA_TITLE', 'H_MEAN', 'A_MEAN', 'OCC_TITLE']]
    all_cities_data.append(final_df)

# Concatenate all city DataFrames into one DataFrame
combined_df = pd.concat(all_cities_data, ignore_index=True)

# Save the combined DataFrame to a single CSV file
combined_csv_file_name = 'combined_occupations.csv'
combined_df.to_csv(combined_csv_file_name, index=False)

print(f"All data combined and saved to {combined_csv_file_name}")
