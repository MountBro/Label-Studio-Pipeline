# Import the SDK and the client module
from label_studio_sdk import Client
import requests
import os
import asyncio
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMG_PATH, PROJ_ID


async def uploadImg(path):
    # Upload the files in ./img
    headers = {
        'Authorization': 'Token ' + API_KEY,
    }
    files = {
        'FileUpload': (IMG_PATH+path, open(IMG_PATH+path, 'rb')),
    }
    # FIXME add project choice
    return requests.post(LABEL_STUDIO_URL+'/api/projects/'+str(PROJ_ID)+'/import',
                         headers=headers, files=files)


async def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
    else:
        print('Connection Succeeds!')
        # Find the files in ./img
        for root, dir, file in os.walk(IMG_PATH):
            break
        response_table = []
        for uploader in asyncio.as_completed(map(uploadImg, file)):
            response_table.append((await uploader).json())
        [print(item) for item in response_table]


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
