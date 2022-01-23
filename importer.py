# Import the SDK and the client module
import asyncio
import os

import requests
from label_studio_sdk import Client

from const import LABEL_STUDIO_URL, API_KEY, IMPORT_PATH, PROJ_ID


async def upload_img(path):
    # Upload the files in ./img
    headers = {
        'Authorization': 'Token ' + API_KEY,
    }
    files = {
        'FileUpload': (IMPORT_PATH + path, open(IMPORT_PATH + path, 'rb')),
    }
    return requests.post(LABEL_STUDIO_URL + '/api/projects/' + str(PROJ_ID) + '/import',
                         headers=headers, files=files)


async def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
    else:
        print('Connection Succeeds!')
        # Find the files in ./img
        for root, directory, file in os.walk(IMPORT_PATH):
            break
        response_table = []
        for uploader in asyncio.as_completed(map(upload_img, file)):
            response_table.append((await uploader).json())
        [print(item) for item in response_table]


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
