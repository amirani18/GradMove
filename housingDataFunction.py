import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def plot_housing_prices_for_city(city):
    # read csv file into pandas dataframe
    housing = pd.read_csv('archive/City_MedianRentalPrice_1Bedroom.csv')
    housing2 = pd.read_csv('archive/City_MedianRentalPrice_2Bedroom.csv')
    housing3 = pd.read_csv('archive/City_MedianRentalPrice_3Bedroom.csv')
    housing4 = pd.read_csv('archive/City_MedianRentalPrice_4Bedroom.csv')

    bedroom_count = 1  # Use a different variable for the filename index
    list_images = []
    for h in [housing, housing2, housing3, housing4]:
        housing_cities = h[h['Metro'] == city]
        if housing_cities.shape[0] > 1:
            for i in range(6, len(housing_cities.columns)):
                housing_cities.loc[housing_cities['Metro'] == city, housing_cities.columns[i]] = housing_cities[housing_cities['Metro'] == city].iloc[:, i].mean()
                housing_cities = housing_cities.drop_duplicates(subset='Metro', keep='first')

        x_values = housing_cities.columns[6:]
        y_values = housing_cities[housing_cities['Metro'] == city].iloc[0, 6:]

        plt.plot(x_values, y_values, label=city, color='pink', linewidth=2.5)
        plt.xlabel('Year-Month')
        plt.ylabel('Price')
        plt.title(f'Median Rental Price {bedroom_count} Bedroom')
        plt.tick_params(axis='x', which='major', labelsize=8)
        plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
        plt.xticks(rotation=45)
        plt.legend()
        
        # Save plot to png
        filename = f'City_MedianRentalPrice_{bedroom_count}Bedroom_Cities_filtered.png'
        plt.savefig(filename)
        list_images.append(filename)
        
        plt.clf()  # Clear the figure for the next plot
        bedroom_count += 1  # Increment the bedroom count for the next filename

    return list_images
       
    
# Example usage
#plot_housing_prices_for_city("New York-Newark-Jersey City")
