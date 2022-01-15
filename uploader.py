# Import the SDK and the client module
from label_studio_sdk import Client
import requests as rq
import os

# Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
IMG_PATH = './img/'

# Connect to the Label Studio API and check the connection
lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
if not lbsd.check_connection()['status'] == 'UP':
    print('Warning: Connection Fails!')
else:
    print('Connection Succeeds!')
    print('')
    # Upload the images in ./img
    for root, dir, file in os.walk(IMG_PATH):
        img_dir = file
        break
    headers = {
        'Authorization': 'Token 181439286e4b2ed9c0026f5e46a27a39858e6905',
    }
    response_list = []
    for img in img_dir:
        files = {
            'FileUpload': (IMG_PATH+img, open(IMG_PATH+img, 'rb')),
        }
        response = rq.post('http://localhost:8080/api/projects/1/import',
                           headers=headers, files=files)
        response_list.append(response)
    # print(response_list)
