# Label Studio Pipeline

This is a [Label Studio](https://github.com/heartexlabs/label-studio) pipeline designed by _Ethan Jia_, licensed by MIT license.

## Installation

- Start Label Studio:

```bash
# Install all package dependencies
pip3 install -e .
# Run database migrations
python3 label_studio/manage.py migrate
# Start the server in development mode at http://localhost:8080
python3 label_studio/manage.py runserver
```

- Clone this repo.
- Install the SDK for Label Studio:

```bash
pip3 install label-studio-sdk
```

## Usage

```bash
python3 uploader.py
```
