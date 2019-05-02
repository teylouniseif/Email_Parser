import json
import requests

# Set the webhook_url to the one provided by recipient
webhook_url = 'https://webhook.site/3ab5de7c-2784-4513-a8ef-cb25d66346f1'

def push_request(data):
    response = requests.post(
        webhook_url, data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
