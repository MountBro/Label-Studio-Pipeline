# Label Studio Pipeline

## Installation

安装 Label Studio 的 SDK 包：

```bash
pip3 install label-studio-sdk
```

## Usage

### Account Token

1. 在 Label Studio UI 界面, 点击右上角的用户头像.
2. 选择 **Account & Settings**.
3. 拷贝 access token.

### Uploader

上传之前，请在 `uploader.py` 中修改以下变量:

```python
# Label Studio的url
LABEL_STUDIO_URL = 'http://localhost:8080'
# API token
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
# 图像存储的文件夹
IMG_PATH = './img/'
```

Then start the uploading:

```bash
python3 uploader.py
```

### Syncer

```bash
python3 syncer.py
```
