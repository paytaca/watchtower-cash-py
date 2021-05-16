import requests


def subscribe(address, webhook_url=''):
    url = 'https://watchtower.cash/api/webhook/subscribe'
    payload = {
        'address': address,
        'web_url': webhook_url
    }
    resp = requests.post(
        json=payload
    )
    result = 'failed'
    if resp.status_code == 200:
        result = 'success'
    return result
