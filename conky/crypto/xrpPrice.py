#!/usr/bin/env python3

# This file utilizes the coinMarketCap API and pulls the price in GBP.

import requests
import time
import json

def getRipplePrice():
    apiUrl = 'https://api.coinmarketcap.com/v1/ticker/ripple/?convert=GBP'

    jsonData = requests.get(apiUrl).json()

    xrpPriceRaw = float(jsonData[0]['price_gbp'])

    xrpPrice = round(xrpPriceRaw, 2)

    return xrpPrice

print(str(getRipplePrice()))
