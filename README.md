# Label Studio Pipeline

## Installation

```bash
pip3 install label-studio-sdk
```

## Usage

### Account Token

1. In the Label Studio UI, click the user icon in the upper right.
2. Click **Account & Settings**.
3. Copy the access token. 

### Uploader

Before uploading, please revise the following values in `uploader.py`: 

```python
# The local url for label studio
LABEL_STUDIO_URL = 'http://localhost:8080'
# The API token of your account
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'
# The folder where the image is stored
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

