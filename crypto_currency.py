import requests
import pandas as pd
from datetime import datetime

# API information
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1
}

# Sending the request
response = requests.get(url, params=params)

if response.status_code == 200:
    print('Connection Successful! \nGetting the data...')
    
    # Storing the response into data
    data = response.json()
    
    # Creating the dataframe
    df = pd.DataFrame(data)
    
    # Check if all required columns exist
    required_columns = [
        'id', 'current_price', 'market_cap', 
        'price_change_percentage_24h', 'ath', 'atl'
    ]
    
    # Ensure only the required columns are selected, adding NaN if missing
    df = df.reindex(columns=required_columns)
    
    # Creating a new column for the timestamp
    today = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    df['time_stamp'] = today
    
    # Get the top 10 cryptocurrencies with the most negative price change
    top_negative = df.sort_values(by='price_change_percentage_24h', ascending=True)
    top_negative_10 = top_negative.head(10)
    top_negative_10.to_csv(f'top_negative_10_{today}.csv', index=False)
    
    # Get the top 10 cryptocurrencies with the most positive price change
    top_positive = df.sort_values(by='price_change_percentage_24h', ascending=False)
    top_positive_10 = top_positive.head(10)
    top_positive_10.to_csv(f'top_positive_10_{today}.csv', index=False)
    
    # Save the full dataset to a CSV file
    df.to_csv(f'crypto_data_{today}.csv', index=False)
    
    # Print results
    print(f'Top 10 cryptocurrencies with the highest price decrease (%):\n{top_negative_10}')
    print(f'Top 10 cryptocurrencies with the highest price increase (%):\n{top_positive_10}')
    print('Data saved successfully!')
    
else:
    print(f'Connection failed. Error Code: {response.status_code}')
