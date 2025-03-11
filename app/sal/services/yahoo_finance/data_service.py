
import os
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yfin
from pandas_datareader import data as pdr

yfin.pdr_override()

class YahooFinanceDataService:
      
      def __init__(self):
            pass

      def fetch_data(self, ticker, start_date, end_date=dt.datetime.now(), interval='1d'):
            # Hourly data request range must be within the last 730 days.
            df = pdr.get_data_yahoo(ticker, start=start_date, end=end_date, interval=interval)
            return df