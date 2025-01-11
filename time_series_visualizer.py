import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data
def load_and_clean_data():
    df = pd.read_csv("C:/Users/dixit/Desktop/Project 2025/Github/time-series visualizer/fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
    # Filter out the top and bottom 2.5%
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    return df

def draw_line_plot():
    # Load data
    df = load_and_clean_data()

    # Draw the line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Add title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Load data
    df = load_and_clean_data()

    # Prepare data for bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.title("Monthly Average Page Views per Year")

    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Load data
    df = load_and_clean_data()

    # Prepare data for box plots
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    df['month_num'] = df.index.month
    df = df.sort_values('month_num')

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig

if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
