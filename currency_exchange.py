import urllib.request
import json

data_cad = []
data_usd = []


def btc_exchange():
    for value in range(7):
        URL = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2024-07-0{2+value}/v1/currencies/btc.json'
        response = urllib.request.urlopen(URL)
        results = json.loads(response.read())
        data_cad.append(results['btc']['cad'])
        data_usd.append(results['btc']['usd'])
    return data_cad, data_usd

