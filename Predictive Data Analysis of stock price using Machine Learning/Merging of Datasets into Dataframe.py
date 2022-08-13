"""
Twiiter sentiment dataset:
https://www.kaggle.com/nadun94/twitter-sentiments-aapl-stock

Stock price data set
https://finance.yahoo.com/quote/AAPL/history?p=AAPL
"""

import pandas

stock_prices_dataframe = pandas.read_csv("stock_prices.csv")

stock_prices_dataframe

twitter_sentiment_dataframe = pandas.read_csv("twitter_sentiment.csv")

twitter_sentiment_dataframe

twitter_sentiment_dataframe.info()

twitter_sentiment_dataframe = twitter_sentiment_dataframe.dropna(axis = 1)

twitter_sentiment_dataframe

stock_prices_dataframe = stock_prices_dataframe.dropna(axis = 1)

stock_prices_dataframe

merged_dataframe = stock_prices_dataframe.merge(twitter_sentiment_dataframe, 
                                                on = "Date")

merged_dataframe

merged_dataframe.to_csv("merged_stocks_and_twitter_sentiment.csv", 
                        index = False)