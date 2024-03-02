import pandas as pd

# Read combined_occupations.csv into df
df = pd.read_csv('combined_occupations.csv')


# if AREA_TITLE is Atlanta-Sandy Springs-Roswell, GA rename it with 'ATLANTA'
df.loc[df['AREA_TITLE'] == 'Atlanta-Sandy Springs-Roswell, GA', 'AREA_TITLE'] = 'ATLANTA'
df.loc[df['AREA_TITLE'] == 'Dallas-Fort Worth-Arlington, TX', 'AREA_TITLE'] = 'FORT_WORTH'
df.loc[df['AREA_TITLE'] == 'Chicago-Naperville-Elgin, IL-IN-WI', 'AREA_TITLE'] = 'CHICAGO'
df.loc[df['AREA_TITLE'] == 'New York-Newark-Jersey City, NY-NJ-PA', 'AREA_TITLE'] = 'NEW_YORK'
df.loc[df['AREA_TITLE'] == 'Kansas City, MO-KS', 'AREA_TITLE'] = 'KANSAS_CITY'
df.loc[df['AREA_TITLE'] == 'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD', 'AREA_TITLE'] = 'PHILADELPHIA'
df.loc[df['AREA_TITLE'] == 'Denver-Aurora-Lakewood, CO', 'AREA_TITLE'] = 'DENVER'
df.loc[df['AREA_TITLE'] == 'Seattle-Tacoma-Bellevue, WA', 'AREA_TITLE'] = 'SEATTLE'
df.loc[df['AREA_TITLE'] == 'Boston-Cambridge-Nashua, MA-NH', 'AREA_TITLE'] = 'CAMBRIDGE'
df.loc[df['AREA_TITLE'] == 'San Francisco-Oakland-Hayward, CA', 'AREA_TITLE'] = 'SAN_FRANCISCO'


# Print the updated dataframe
new_combined_csv_file_name = 'combined_occupations2.csv'
df.to_csv(new_combined_csv_file_name, index=False)