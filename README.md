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
# API token （以下是我本地label studio的token）
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
# 导入导出的文件夹
EXPORT_PATH = './export/'
IMPORT_PATH = './img/'
# project ID
PROJ_ID = 1
```

## Importer

此功能支持以下上传格式:

- `*.png`
- `*.jpg`
- `*.JSON` (即，标注过的图片使用导出功能生成的JSON文件)

```bash
python3 importer.py
```

### Exporter

此功能支持导出**已标注的**图片信息，包括点位和具体文件名etc，将导出成JSON格式。

```bash
python3 exporter.py
```

### Syncer

官方sync的API暂时[deprecated](https://github.com/heartexlabs/label-studio/issues/1873)，正在造自动同步的轮子

```bash
python3 syncer.py
```