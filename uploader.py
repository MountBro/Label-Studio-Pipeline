# Import the SDK and the client module
from label_studio_sdk import Client
import requests as rq
import os
import asyncio

#  Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
IMG_PATH = './img/'


async def uploadImg(path):
    # Upload the images in ./img
    headers = {
        'Authorization': 'Token ' + API_KEY,
    }
    files = {
        'FileUpload': (IMG_PATH+path, open(IMG_PATH+path, 'rb')),
    }
    return rq.post('http://localhost:8080/api/projects/1/import',
                   headers=headers, files=files)


async def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Warning: Connection Fails!')
    else:
        print('Connection Succeeds!')
        # Find the images in ./img
        for root, dir, file in os.walk(IMG_PATH):
            break
        response_table = []
        for uploader in asyncio.as_completed(map(uploadImg, file)):
            response_table.append((await uploader).json())
        # print(response_table)
        [print(item) for item in response_table]


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
