# Get the project tasks

import requests
from label_studio_sdk import Client
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMPORT_PATH, PROJ_ID

headers = {
    'Authorization': 'Token ' + API_KEY,
}

data = {
    "project": "1",
    "url": "https://webhook.site/3cad2046-88c4-424c-b826-68e5c25361d8",
    "send_payload": "true",
    "send_for_all_actions": "true",
    "is_active": "true",
    "actions": []
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
    response = requests.get(
        # 'http://localhost:8080/api/webhooks', headers=headers, json=data)
        'http://localhost:8080/api/webhooks/info')
    print(response.json())
