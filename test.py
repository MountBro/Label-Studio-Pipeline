# Get the project tasks

import requests
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMPORT_PATH, PROJ_ID

headers = {
    'Authorization': 'Token '+API_KEY,
}

proxies = {
    'http': 'http://localhost:8080'
}

response = requests.get(
    'http://localhost:8080/api/projects/1/tasks/', headers=headers)
print(response.json())
