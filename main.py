import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# fixed url
url = "https://cache.showwcase.com/user/" + "sahil-sagwekar2652"

# API Headers
headers = {'Authorization': 'Bearer ' + os.getenv('API_KEY')}


# API Request
response = requests.get(url, headers=headers)

print(response.text)
