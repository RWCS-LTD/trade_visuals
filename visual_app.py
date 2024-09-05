import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def analyze_data(df):
    # Ensure the Date/Time column is correctly parsed
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')

    # Extract additional time-based features
    df['DayOfWeek'] = df['Date/Time'].dt.day_name()
    df['HourOfDay'] = df['Date/Time'].dt.hour

    # Heatmap for Average Profit Percentage by Day and Hour
    heatmap_data = df.pivot_table(values='Profit %', index='DayOfWeek', columns='HourOfDay', aggfunc='mean')
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title('Heat Map for Average Profit Percentage by Day and Hour')
    st.pyplot(plt.gcf())

    # Profit Distribution by Day of the Week
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='DayOfWeek', y='Profit USD', data=df)
    plt.title('Profit Distribution by Day of the Week')
    st.pyplot(plt.gcf())

    # Profit Distribution by Hour of the Day
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='HourOfDay', y='Profit USD', data=df)
    plt.title('Profit Distribution by Hour of the Day')
    st.pyplot(plt.gcf())

    # Cumulative Profit Over Time
    df = df.sort_values('Date/Time')  # Ensure data is sorted by time
    df['Cum. Profit USD'] = df['Profit USD'].cumsum()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date/Time'], df['Cum. Profit USD'], marker='o')
    plt.title('Cumulative Profit Over Time')
    plt.xlabel('Date/Time')
    plt.ylabel('Cumulative Profit USD')
    st.pyplot(plt.gcf())

    # Profit Heatmap for Opening and Closing Positions
    open_close_heatmap_data = df.pivot_table(values='Profit USD', index='Type', columns='Signal', aggfunc='mean')
    plt.figure(figsize=(10, 8))
    sns.heatmap(open_close_heatmap_data, annot=True, fmt=".2f", cmap="viridis")
    plt.title('Profit Heatmap for Opening and Closing Positions')
    st.pyplot(plt.gcf())

    # Scatter Plot of Profit vs Drawdown
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Drawdown USD'], df['Profit USD'], alpha=0.7)
    plt.title('Scatter Plot of Profit vs Drawdown')
    plt.xlabel('Drawdown USD')
    plt.ylabel('Profit USD')
    st.pyplot(plt.gcf())

    # Histogram of Profit Percentages
    plt.figure(figsize=(10, 6))
    plt.hist(df['Profit %'].dropna(), bins=30, alpha=0.7)
    plt.title('Histogram of Profit Percentages')
    plt.xlabel('Profit %')
    plt.ylabel('Frequency')
    st.pyplot(plt.gcf())

def main():
    st.title('Trade Data Analyzer')

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Add a note below the file uploader
    st.write("**Note:** Upload CSV file directly downloaded from TradingView's 'List of Trades' tab in the backtesting engine on TradingView. This will allow additional and alternative visualizations from your strategy's performance.")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        analyze_data(df)

if __name__ == "__main__":
    main()
