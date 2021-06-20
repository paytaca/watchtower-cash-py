import requests


def subscribe(address, project_id, wallet_hash=None, webhook_url=None):
    url = 'https://watchtower.cash/api/webhook/subscribe/'
    payload = {
        'address': address,
        'web_url': webhook_url
    }
    resp = requests.post(
        url,
        json=payload
    )
    return resp.json()
