import requests


class Wallet(object):

    def __init__(self, testnet=False):
        if testnet:
            self.base_url = 'https://testnet.watchtower.cash/api/'
        else:
            self.base_url = 'https://watchtower.cash/api/'

    def _get_utxos(self, wallet_hash, amount):
        url = self.base_url + f'utxo/wallet/{wallet_hash}'
        resp = requests.get(url)
        print(resp.status_code)
        print(resp.json())

    def send(self, amount):
        self._get_utxos('abcd0123456', amount)
        print(f"Sending {amount} BCH...")
