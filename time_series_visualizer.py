import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', sep=',', parse_dates=True)
print(df)
# Clean data
print("2.5% percentile: {}".format(df['value'].quantile(0.025)))
print("bottom of 2.5% percentile: {}".format(df['value'].quantile(0.975)))

df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]
print(df)

def draw_line_plot():
    # Draw line plot
    fig, axes= plt.subplots(figsize=(16,5))
    plt.plot(df, color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=12)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
