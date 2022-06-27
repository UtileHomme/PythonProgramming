import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


#
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

        json_data = json.dumps(data)

        r = requests.get(url=URL, data=json_data)

        data = r.json()
        print(data)


get_data(2)


def post_data():
    data = {
        'name': 'Jatin',
        'roll': 102,
        'city': 'Ranchi'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    print(r)
    data1 = r.json()
    print(data1)


# post_data()


def update_data():
    data = {
        'id': '6',
        'name': 'Rohit Sharma',
        'city': 'Ranchi1'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    print(r)
    data1 = r.json()
    print(data1)


# update_data()

def delete_data():
    data = {
        'id': 7
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    print(r)
    data1 = r.json()
    print(data1)


delete_data()
