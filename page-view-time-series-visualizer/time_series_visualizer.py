import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
cond = (df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))
df = df.loc[cond]

df_temp = df.copy()
df_temp[(['year', 'month', 'day'])] = df_temp['date'].str.split('-', expand = True).astype(int)

df['date'] = pd.to_datetime(df['date'])

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 10))
    plt.plot(df['date'], df['value'], color = 'red', linewidth = 3)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize = 26)
    ax.set_xlabel('Date', fontsize = 22)
    ax.set_ylabel('Page Views', fontsize = 22)
    ax.tick_params(axis = 'both', labelsize = 20)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_temp.groupby(['year', 'month'])['value'].mean().reset_index().astype(int)

    # Draw bar plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (15,13))
    position = 0
    width = 0.5
    colors = plt.color_sequences['Paired']
    label_positions = []

    years = sorted(df_bar['year'].unique())
    months = sorted(df_bar['month'].unique())

    for y in years:
        cond1 = df_bar['year'] == y
        c = 0
        for m in months:
            cond2 = df_bar['month'] == m
            value = df_bar.loc[cond1 & cond2, 'value']
            if len(value) == 0:
                value = 0
            ax.bar(x = position, height = value, width = width, color = colors[c])
            c += 1
            if m == 6:
                label_positions.append(position + width/2)
            position += 0.5
        position += 6

    ax.set_ylabel('Average Page Views', fontsize = 22)
    ax.set_xlabel('Years', fontsize = 22)

    legend = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(labels = legend, fontsize = 20, title = 'Months', title_fontsize = 21)
    ax.set_xticks(ticks = label_positions, labels = years) 
    ax.tick_params(axis = 'both', labelsize = 20)
    ax.tick_params(axis = 'x', labelrotation = 90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_temp.copy()

    '''df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]'''

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (28, 10))

    sns.boxplot(data = df_box,
                x = 'year',
                y = 'value',
                hue = 'year',
                palette = 'tab10',
                dodge = False,
                ax = ax1
               )
    ax1.legend(labels = [])
    ax1.set_ylabel('Page Views', fontsize = 22)
    ax1.set_xlabel('Year', fontsize = 22)
    ax1.tick_params(axis = 'both', labelsize = 20)
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize = 24)
    yticks = ax1.get_yticks()
    values_labels = list(range(0, 200001, 20000))
    ax1.set_yticks(yticks, values_labels)


    sns.boxplot(data = df_box,
                x = 'month',
                y = 'value',
                hue = 'month',
                palette = 'Paired',
                dodge = False,
                ax = ax2
               )
    ax2.legend(labels = [])
    ax2.set_ylabel('Page Views', fontsize = 22)
    ax2.set_xlabel('Month', fontsize = 22)
    ax2.tick_params(axis = 'both', labelsize = 20)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize = 24)
    months_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ticks = ax2.get_xticks()
    ax2.set_xticks(ticks, months_labels)
    yticks = ax2.get_yticks()
    ax2.set_yticks(yticks, values_labels)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
