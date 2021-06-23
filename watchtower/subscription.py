import requests
import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def subscribe(address, project_id=None, wallet_hash=None, wallet_index=None, webhook_url=None):
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
            'address': address,
            'project_id': project_id,
            'wallet_hash': wallet_hash,
            'wallet_index': wallet_index,
            'webhook_url': webhook_url
        }
        resp = requests.post(
            url,
            json=payload
        )
        return resp.json()
    return response
