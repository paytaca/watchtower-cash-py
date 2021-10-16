try:
    import requests
except ImportError:
    pass
import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def subscribe(addresses=None, project_id=None, wallet_hash=None, address_index=None, webhook_url=None):
    response = {'success': False}
    proceed = False
    if project_id:
        if is_valid_uuid(project_id):
            proceed = True
    else:
        response['error'] = 'project_id is invalid UUID'
    if proceed:
        url = 'https://watchtower.cash/api/subscription/'
        payload = {
            'addresses': addresses,
            'project_id': project_id,
            'wallet_hash': wallet_hash,
            'address_index': address_index,
            'webhook_url': webhook_url
        }
        resp = requests.post(
            url,
            json=payload
        )
        return resp.json()
    return response
