# Label Studio Pipeline

## Installation

安装 Label Studio 的 SDK 包：

```bash
pip3 install label-studio-sdk
```

## Usage

### API Token

1. 在 Label Studio UI 界面, 点击右上角的用户头像.
2. 选择 **Account & Settings**.
3. 拷贝 access token.

### 全局变量

上传之前，请在 `uploader.py` 中修改以下变量:

```python
# Label Studio的url
LABEL_STUDIO_URL = 'http://localhost:8080'
# API token
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
# 导入导出的文件夹
EXPORT_PATH = './export/'
IMPORT_PATH = './img/'
# project ID
PROJ_ID = 1
```

## Uploader

Then start the uploading:

```bash
python3 uploader.py
```

### Exporter

```bash
python3 exporter.py
```

### Syncer

功能暂时deprecated

```bash
python2 syncer.py
```