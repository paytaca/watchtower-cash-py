# watchtower-cash-py

Library for building Python applications that integrate with Watchtower.cash

### Install
```bash
pip install watchtower-cash-py
```

### Subscribe an Address
For Watchtower to keep watch of the transactions of an address, it needs to be subscribed. A convenient function is included here to subscribe an address.
```python
import watchtower

# Subscribe function accepts either BCH or SLP address
data = {
    'address': address, #'simpleledger:qqz95enwd6qdcy5wnf05hp590sjjknwfuq8sjhpv6x',
    'project_id': x, #'0000-0000-0000',  # <-- Generate this ID by creating a project at Watchtower.cash
    'wallet_hash': 'abcd0123456', # <-- (Optional) You generate this to track which HD wallet the address belongs to
    'wallet_index': 0, # <-- (Optional) The index used to generate this address from HD wallet
    'webhook_url': 'https://xxx.com/webhook-call-receiver'  # <-- (Optional) Your webhook receiver URL
}

result = watchtower.subscribe(**data)
```
