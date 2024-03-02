import pandas as pd
import matplotlib.pyplot as plt

# read csv file into pandas dataframe
housing = pd.read_csv('/Users/shreya/Purdue/InnovateHer/GradMove/GradMove/archive/City_MedianRentalPrice_1Bedroom.csv')

# print the first 5 rows of the dataframe
print(housing.head())

# extract information for the list of cities below (the cities will be in the column Metro)
cities = ['Atlanta-Sandy Springs-Roswell', 'Dallas-Fort Worth-Arlington', 'Chicago-Naperville-Elgin', 'New York-Newark-Jersey City', 'Kansas City', 
          'Philadelphia-Camden-Wilmington', 'Denver-Aurora-Lakewood', 'Seattle-Tacoma-Bellevue', 'Boston-Cambridge-Newton', 'San Francisco-Oakland-Hayward']

# create a new dataframe with only the cities in the list above
housing_cities = housing[housing['Metro'].isin(cities)]

# if there is more than one row 
# with the same Metro name
# for each row with the same Metro name
# keep the one that has the highest value in the column 2019-12
housing_cities = housing_cities.sort_values('2019-12', ascending=False).drop_duplicates('Metro')



# make a time series plot for each city in the list above
# of how the rental price has changed over time

# for wach city in cities
# in all the numerical columns that are not empty, plot the values

for city in cities:
    # x axis is the year-month column
    # y axis is the value of the column
    # title is the name of the city
    # plot the values
    x_values = housing_cities.columns[6:]
    y_values = housing_cities[housing_cities['Metro'] == city].iloc[0, 6:]
    plt.plot(x_values, y_values, label=city)
    plt.xlabel('Year-Month')
    plt.ylabel('Price')
    plt.title('Median Rental Price 1 Bedroom')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()
    
    
# save this into a new csv
housing_cities.to_csv('/Users/shreya/Purdue/InnovateHer/GradMove/GradMove/City_MedianRentalPrice_1Bedroom_Cities_filtered.csv', index=False)