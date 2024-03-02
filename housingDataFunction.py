import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def plot_housing_prices_for_city(city):
    # read csv file into pandas dataframe
    housing = pd.read_csv('/Users/shreya/Purdue/InnovateHer/GradMove/GradMove/archive/City_MedianRentalPrice_1Bedroom.csv')

    housing_cities = housing[housing['Metro'] == city]
    if housing_cities.shape[0] > 1:
        for i in range(6, len(housing_cities.columns)):
            housing_cities.loc[housing_cities['Metro'] == city, housing_cities.columns[i]] = housing_cities[housing_cities['Metro'] == city].iloc[:, i].mean()
            housing_cities = housing_cities.drop_duplicates(subset='Metro', keep='first')

    x_values = housing_cities.columns[6:]
    y_values = housing_cities[housing_cities['Metro'] == city].iloc[0, 6:]
    plt.plot(x_values, y_values, label=city, color = 'pink', linewidth = 2.5)
    plt.xlabel('Year-Month')
    plt.ylabel('Price')
    plt.title('Median Rental Price 1 Bedroom')
    plt.tick_params(axis='x', which='major', labelsize=8)
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # save this into a new csv
    housing_cities.to_csv('/Users/shreya/Purdue/InnovateHer/GradMove/GradMove/City_MedianRentalPrice_1Bedroom_Cities_filtered.csv', index=False)    
    
# Example usage
plot_housing_prices_for_city("New York-Newark-Jersey City")
