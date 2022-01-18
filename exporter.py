import requests as rq
from label_studio_sdk import Client
from ProgressBar import ProgressBar
from contextlib import closing


# Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
IMG_PATH = './img/'
FILE_NAME = 'export.json'

headers = {
    'Authorization': 'Token ' + API_KEY,
}
params = (
    ('exportType', 'JSON'),
)

with closing(rq.get(LABEL_STUDIO_URL + '/api/projects/1/export', stream=True, headers=headers, params=params)) as response:
    print(response.json())
    chunk_size = 1024  # 单次请求最大值
    content_size = int(response.headers['content-length'])  # 内容体总大小
    progress = ProgressBar(FILE_NAME, total=content_size,
                           unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
    with open(FILE_NAME, "wb") as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            progress.refresh(count=len(data))
