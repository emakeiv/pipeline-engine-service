import oandapyV20
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments

from oandapyV20 import API
from oandapyV20.contrib.factories import InstrumentsCandlesFactory

import datetime
import pandas as pd

class OandaDataService():

    def __init__(self, access_token, account_id, environment='practice', headers=None, request_params=None):
        self.name = 'oanda'
        self.token = access_token
        self.account_id = account_id
        self.environment = environment
        self.client = API(
            access_token=access_token
        )
    
    def get_list_of_instruments(self):
         pass
    
    def fetch_data(self, instrument, start_date, granularity='D'):
        format = '%Y-%m-%dT%H:%M:%SZ'
        params = {
            "from": start_date.strftime(format),
            "granularity": granularity,
            "count": 2500,  # Maximum number of data points
        }

        full_data = []
        for response in InstrumentsCandlesFactory(instrument=instrument, params=params):
            self.client.request(response)
            candles = response.response.get('candles')
            if candles:
                for candle in candles:
                    candle_data = [
                        candle['time'], 
                        candle['volume'],
                        candle['mid']['o'], 
                        candle['mid']['h'],
                        candle['mid']['l'], 
                        candle['mid']['c']
                    ]
                    full_data.append(candle_data)

        df = pd.DataFrame(full_data, columns=['time', 'volume', 'open', 'high', 'low', 'close'])
        df['time'] = pd.to_datetime(df['time'])
        valid_rows = df.dropna()
    
        if len(valid_rows) != len(df):
            print(f"there are missing data for {len(df) - len(valid_rows)} rows")

        df.set_index('time', inplace=True)
        return df