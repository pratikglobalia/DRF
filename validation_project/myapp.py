import json
import requests

URL = 'http://127.0.0.1:8000/'

def get_data(id=None):
    data = {}
    if data is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
# get_data(1)

def post_data():
    data = {
        'name':'ratik',
        'roll':198,
        'city':'junagadh'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
post_data()

def put_data():  
    data = {
        'id':2,
        'name':'anshkumar',
        'city':'somnath'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
# put_data()

def delete_data():
    data = {'id':4}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
# delete_data()