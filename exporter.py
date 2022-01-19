import os
import time
import requests
from label_studio_sdk import Client
from ProgressBar import ProgressBar
from contextlib import closing
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMPORT_PATH, PROJ_ID


headers = {
    'Authorization': 'Token ' + API_KEY,
}
params = (
    ('exportType', 'JSON'),
)


def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
        pass
    else:
        print('Connection Succeeds!')
        with closing(requests.get(LABEL_STUDIO_URL + '/api/projects/'+str(PROJ_ID)+'/export', stream=True, headers=headers, params=params)) as response:
            # print(response.json())
            now = int(round(time.time()*1000))
            file_name = time.strftime('%Y-%m-%d-%H:%M:%S',
                                      time.localtime(now/1000))+'.json'
            chunk_size = 1024  # 单次请求最大值byte
            content_size = int(response.headers['content-length'])  # 内容体总大小
            progress = ProgressBar(file_name, total=content_size,
                                   unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
            if not os.path.exists(EXPORT_PATH):
                os.makedirs(EXPORT_PATH)
            with open(EXPORT_PATH+file_name, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    progress.refresh(count=len(data))


if __name__ == '__main__':
    main()
