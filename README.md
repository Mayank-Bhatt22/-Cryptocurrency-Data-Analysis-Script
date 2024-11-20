# -Cryptocurrency-Data-Analysis-Script
This Python script is designed to fetch and analyze real-time cryptocurrency market data using the CoinGecko API. It retrieves data about the top cryptocurrencies by market capitalization and processes the information to highlight key trends in price changes. Here's an overview of its functionality
Features:
API Integration:

Connects to the CoinGecko API to fetch data about cryptocurrencies, including their current prices, market capitalization, price changes over the last 24 hours, all-time highs (ATH), and all-time lows (ATL).
Data Processing with Pandas:

Converts the fetched JSON data into a Pandas DataFrame for easier manipulation and analysis.
Ensures that the relevant columns (id, current_price, market_cap, price_change_percentage_24h, ath, and atl) are included, handling missing columns gracefully.
Sorting and Analysis:

Identifies the top 10 cryptocurrencies with the most significant price decreases and price increases over the past 24 hours.
Sorts the data based on the price_change_percentage_24h column to determine the gainers and losers in the market.
Data Export:

Saves three CSV files:
The full dataset (crypto_data_<timestamp>.csv).
The top 10 cryptocurrencies with the highest price decreases (top_negative_10_<timestamp>.csv).
The top 10 cryptocurrencies with the highest price increases (top_positive_10_<timestamp>.csv).
Each file is timestamped to ensure data versioning and easy retrieval.
Timestamp Logging:

Adds a timestamp column (time_stamp) to the dataset for tracking when the data was fetched and analyzed.
User-Friendly Output:

Prints the top 10 gainers and losers directly in the console for quick insights.
Error Handling:
Verifies the success of the API request by checking the HTTP response status.
Prints an error message if the API request fails, helping users diagnose issues with connectivity or the API service.
Applications:
Ideal for data analysts, cryptocurrency traders, or enthusiasts looking to monitor market trends efficiently.
Provides a foundation for further analysis, such as building visualizations or developing trading algorithms.
This script demonstrates the practical use of Python for data acquisition, analysis, and report generation in a real-world scenario, leveraging tools like Pandas and requests for robust data handling.
