import time
import asyncio

from label_studio_sdk import Client
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from const import LABEL_STUDIO_URL, API_KEY
from importer import upload_img

watch_patterns = "*.py;*.txt"  # 监控文件的模式
ignore_patterns = ""  # 设置忽略的文件模式
ignore_directories = False  # 是否忽略文件夹变化
case_sensitive = True  # 是否对大小写敏感
event_handler = PatternMatchingEventHandler(
    watch_patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    print(str(event.src_path) + "被创建")
    asyncio.run(upload_img(event.src_path))


def on_deleted(event):
    print(f"{event.src_path}被删除")


def on_modified(event):
    print(f"{event.src_path} 被修改")


def on_moved(event):
    print(f"{event.src_path}被移动到{event.dest_path}")


event_handler.on_created = on_created
event_handler.on_deleted = on_deleted
event_handler.on_modified = on_modified
event_handler.on_moved = on_moved

watch_path = "/home/ethanjia/dev/label-studio-pipeline/import"  # 监控目录
go_recursively = True  # 是否监控子文件夹
my_observer = Observer()
my_observer.schedule(event_handler, watch_path, recursive=go_recursively)


def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
        pass
    else:
        print('Connection Succeeds!')
        my_observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            my_observer.stop()
        my_observer.join()


if __name__ == '__main__':
    main()
