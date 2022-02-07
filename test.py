# Get the project tasks

import requests
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMPORT_PATH, PROJ_ID

headers = {
    'Authorization': 'Token ' + API_KEY,
    "project": 0,
    "url": "",
    "send_payload": True,
    "send_for_all_actions": True,
    "headers": {},
    "is_active": True,
    "actions": []
}

proxies = {
    'http': 'http://localhost:8080'
}

if __name__ == 'main':
    response = requests.post(
        'http://localhost:8080/api/webhooks', headers=headers)
    print(response.json())
