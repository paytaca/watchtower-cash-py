import requests

class Type1(object):

    def __init__(self, testnet=False):
        if testnet:
            self.base_url = 'https://testnet.watchtower.cash/api/'
        else:
            self.base_url = 'https://watchtower.cash/api/'

    def _get_utxos(self, address, amount):
        url = self.base_url + f'utxo/slp/{address}'
        resp = requests.get(url)
        print(resp.status_code)
        print(resp.json())

    def send(self, amount):
        self._get_utxos('x', amount)
        print(f"Sending {amount} XXX tokens...")
