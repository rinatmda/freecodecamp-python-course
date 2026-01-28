import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 6))
    ax.scatter(x = df['Year'], 
                y = df['CSIRO Adjusted Sea Level'],
                s = 13
               )

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    x = range(df['Year'][0], 2051)
    y = slope * x + intercept
    ax.plot(x, y, color = 'green')    

    # Create second line of best fit
    cond = df['Year'] >= 2000
    slope_new, intercept_new, r, p, se = linregress(x = df.loc[cond, 'Year'], y = df.loc[cond, 'CSIRO Adjusted Sea Level'])
    x_new = range(2000, 2051)
    y_new = slope_new * x_new + intercept_new
    ax.plot(x_new, y_new, color = 'red')

    # Add labels and title
    ax.set_xlabel('Year', fontsize = 16)
    ax.set_ylabel('Sea Level (inches)', fontsize = 16)
    ax.set_title('Rise in Sea Level', fontsize = 18)
    ax.tick_params(axis = 'both', labelsize = 14)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()