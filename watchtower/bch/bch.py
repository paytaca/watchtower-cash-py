from bitcash.transaction import create_p2pkh_transaction
from bitcash import Key
import requests


class BCH(object):

    def __init__(self, testnet=False):
        if testnet:
            self.base_url = 'https://testnet.watchtower.cash/api/'
        else:
            self.base_url = 'https://watchtower.cash/api/'

    def _get_unspents(self, address, amount):
        url = self.base_url + f'utxo/bch/{address}'
        resp = requests.get(url)
        unspents = []
        return unspents
    
    def _format_outputs(self, recipients):
        outputs = []
        return outputs

    def _broadcast_transaction(self, transaction):
        response = {'success': False}
        response['txid'] = ''
        return response

    def send(self, sender, amount, recipients, broadcast=True):
        print(f"Sending {amount} BCH...")
        unspents = self._get_utxos(sender['address'], amount)
        outputs = []

        private_key = Key(sender['wif'])
        tx_hex = create_p2pkh_transaction(
            private_key,
            unspents,
            outputs
        )

        response = {'success': False}
        if broadcast:
            result = self._broadcast_transaction(tx_hex)
            return result
        else:
            response['success'] = True
            response['transaction'] = tx_hex
            return response
