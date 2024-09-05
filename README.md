# Trade Data Analyzer Streamlit App

This Streamlit app analyzes trade data and provides various visualizations to help understand trading performance. The app is designed to work with CSV files directly downloaded from TradingView's 'List of Trades' tab in the backtesting engine.

## Features

- Heatmap for Average Profit Percentage by Day and Hour
- Profit Distribution by Day of the Week
- Profit Distribution by Hour of the Day
- Cumulative Profit Over Time
- Profit Heatmap for Opening and Closing Positions
- Scatter Plot of Profit vs Drawdown
- Histogram of Profit Percentages

## Installation

1. Clone the repository:

git clone https://github.com/your-username/trade-data-analyzer.git cd trade-data-analyzer

2. Install the required dependencies:

pip install -r requirements.txt

## Usage

Run the Streamlit app:

streamlit run visual_app.py

## Notes

Upload a CSV file directly downloaded from TradingView's 'List of Trades' tab in the backtesting engine. This will allow additional and alternative visualizations from your strategy's performance.

