# Import the SDK and the client module
from label_studio_sdk import Client

# Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = '181439286e4b2ed9c0026f5e46a27a39858e6905'

# Connect to the Label Studio API and check the connection
ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
ls.check_connection()
print(ls.get_projects())
