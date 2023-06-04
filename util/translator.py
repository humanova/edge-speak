import requests
import uuid
import json
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

TRANSLATOR_ENDPOINT = config['translator_endpoint']
SUBSCRIPTION_KEY = config['translator_subscription_key']
REGION = config['translator_region']

def translate_text(text, to_lang):
    endpoint_url = TRANSLATOR_ENDPOINT + '/translate'

    params = {
        'api-version': '3.0',
        'to': to_lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Ocp-Apim-Subscription-Region': REGION,
	
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    response = requests.post(endpoint_url, params=params, headers=headers, json=body)
    response.raise_for_status()

    response_data = json.loads(response.content)
    return response_data[0]