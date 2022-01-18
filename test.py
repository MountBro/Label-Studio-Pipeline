import requests

headers = {
    'Authorization': 'Token 181439286e4b2ed9c0026f5e46a27a39858e6905',
}
files = {
    'file': ('./export/2022-01-18-18:04:25.json', open('./export/2022-01-18-18:04:25.json', 'rb')),
}
proxies = {
    'http': 'https://localhost:8080'
}

response = requests.post(
    'https://localhost:8080/api/projects/1/import', headers=headers, files=files, proxies=proxies)
print(response.json())
