import json

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

# Data in python
data = {
    'name': 'Jatin',
    'roll': 102,
    'city': 'Ranchi'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)
print(r)
data = r.json()
print(data)
