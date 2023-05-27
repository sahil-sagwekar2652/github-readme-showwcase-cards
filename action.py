import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# fixed url
url = "https://cache.showwcase.com/user/" + "atapas398"

# API Headers
headers = {'Authorization': 'Bearer ' + os.getenv('API_KEY')}


# API Request
response = requests.get(url, headers=headers)

with open("output.txt", 'w') as file:
	file.write(response.text)
	file.close()
