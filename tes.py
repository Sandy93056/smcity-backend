import requests
import json

from requests.api import request
# url = "http://127.0.0.1:8000/adddata/"
url = "http://127.0.0.1:8000/customer/login/"
# headers = {'Content-type': 'application/json'}
# headers = {'Authorization': <type> <credentials>}
from requests.structures import CaseInsensitiveDict
headers = CaseInsensitiveDict()
headers["Authorization"] = "token: {0f5805b276f5a1a9f00fc6219e2031e28c5e4d1c}"
data = {
    "username":"admin",
    "password":"admin"
}
json_data = json.dumps(data)
# r = requests.post(url = url, data=json_data, headers=headers)
# r = requests.post(url = url)
# r = requests.get(url = url)
r = requests.get(url=url, headers=headers)

data = r.json()
print(data)