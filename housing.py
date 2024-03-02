import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# read csv file into pandas dataframe
housing = pd.read_csv('City_MedianRentalPrice_1Bedroom_Cities_filtered.csv')

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
# for all the numerical columns, take the mean of the values, and keep only one row

for city in cities:
    # for each city in the list above
    # keep only one row
    # for all the numerical columns, take the mean of the values
    if housing_cities[housing_cities['Metro'] == city].shape[0] > 1:
        # take the mean of all the columns after column 6
        # for each numerical column
        for i in range(6, len(housing_cities.columns)):
            # take the mean of the values and keep only one row
            housing_cities.loc[housing_cities['Metro'] == city, housing_cities.columns[i]] = housing_cities[housing_cities['Metro'] == city].iloc[:, i].mean()
            housing_cities = housing_cities.drop_duplicates(subset='Metro', keep='first')


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
    plt.plot(x_values, y_values, label=city, color='pink', linewidth=2.5)
    plt.xlabel('Year-Month')
    plt.ylabel('Rent per month')
    plt.title('Median Rental Price 1 Bedroom')
    plt.tick_params(axis='x', which='major', labelsize=8)
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
    
    
# save this into a new csv
housing_cities.to_csv('City_MedianRentalPrice_1Bedroom_Cities_filtered.csv', index=False)