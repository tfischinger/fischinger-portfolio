from django.contrib.sites import requests


class CurrencyConverterModel:
    def __init__(self):
        self.api_url = "https://api.apilayer.com/exchangerates_data/convert"
        self.api_key = "pAHkLF6lnwSm9Kx0IN0OW3nnUwdWr3Qf"

    def convert(self, amount, base_currency, target_currency):
        headers = {"apikey": self.api_key}
        params = {
            "from": base_currency,
            "to": target_currency,
            "amount": amount
        }
        response = requests.get(self.api_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('result')
        else:
            return None