# Get the project tasks

import requests
from label_studio_sdk import Client
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMPORT_PATH, PROJ_ID

headers = {
    'Authorization': 'Token ' + API_KEY,
}

data = {
    "project": "1",
    "url": "https://webhook.site/231742c7-3961-4a6d-ae86-252bc34e2ca1",
    "send_payload": "true",
    "send_for_all_actions": "true",
    "is_active": "true",
    "actions": [],
    "headers": headers
}

proxies = {
    'http': 'http://localhost:8080'
}

if __name__ == '__main__':
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
    else:
        print('Connection Succeeds!')
    # response = requests.post(LABEL_STUDIO_URL + '/api/webhooks', data=data)
    # print(response.json())
    response = requests.get(LABEL_STUDIO_URL + '/api/webhooks/')
    print(response.json())
