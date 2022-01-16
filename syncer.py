import asyncio
import json
import os
import requests as rq
from label_studio_sdk import Client


# Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
IMG_PATH = './img/'


def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Warning: Connection Fails!')
    else:
        print('Connection Succeeds!')
    headers = {
        'Authorization': 'Token 181439286e4b2ed9c0026f5e46a27a39858e6905',
        'Content-Type': 'application/json',
    }
    data = {
        "path": "./img/",
        "regex_filter": "",
        "use_blob_urls": True,
        "title": "test sync",
        "description": "test sync",
        "last_sync": "",
        "last_sync_count": 0,
        "project": 0
    }
    response = rq.post(
        'http://localhost:8080/api/projects/1/import', headers=headers, data=json.dumps(data, separators=(',', ':')))
    print(response.json())


if __name__ == '__main__':
    main()
