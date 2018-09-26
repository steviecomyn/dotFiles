#!/usr/bin/env python3

# This file utilizes the coinMarketCap API and pulls the price in GBP.

import requests
import time
import json

def getLitecoinPrice():
    apiUrl = 'https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=GBP'

    jsonData = requests.get(apiUrl).json()

    ltcPriceRaw = float(jsonData[0]['price_gbp'])

    ltcPrice = round(ltcPriceRaw, 2)

    return ltcPrice

print(str(getLitecoinPrice()))
