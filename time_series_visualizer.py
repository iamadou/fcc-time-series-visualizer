import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */
list_months=['January','February','March','April','May','June','July','August','September','October','November','December']
# /* ********************************************************************* */
# /* ********************************************************************* */
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', sep=',', parse_dates=True)
# print(df)
# print(df.shape)
# /* ********************************************************************* */
# /* ********************************************************************* */
# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
#df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]
# print("Bottom Quantile 2.5%: {}".format(df['value'].quantile(0.025)))
# print("Top Quantile 2.5%: {}".format(df['value'].quantile(0.975)))

df_1 = df['value'] <= df['value'].quantile(0.025)
# print("df_1: {} Shape: {}".format(df_1, df_1.shape))
df_2 = df['value'] >= df['value'].quantile(0.975)
# print("df_2: {} Shape: {}".format(df_2, df_2.shape))
cond = (df_1 | df_2)
# print("Resulting df: {} Shape: {}".format(cond, cond.shape))
df = df.drop(index=df[cond].index)
# print("Cleaned df: {} Shape: {}".format(df, df.shape))

# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */

def draw_line_plot():
    # Draw line plot
    fig, axes= plt.subplots(figsize=(14,6))
    plt.plot(df, linestyle="solid", marker=None, color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=12)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')
    # df_grp = df_bar.groupby(['year', 'Month'])
    # series
    # df_grp['value'].apply(lambda x: x.mean())

    # Draw bar plot
    #darkgrid, whitegrid, dark, white, ticks
    sns.set_style("ticks")
    # , palette="rocket"
    g = sns.catplot(x="year", kind="bar", hue="Month", y="value", data=df_bar, hue_order=list_months, ci=None, legend=False, palette="bright")

    fig = g.fig
    ax = g.ax    
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title="Month")
    plt.setp(ax.get_legend().get_texts(), fontsize='9')
    plt.setp(ax.get_legend().get_title(), fontsize='9')
    plt.tight_layout()
    # Draw bar plot

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */
# /* ********************************************************************* */

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    print(df_box)
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
