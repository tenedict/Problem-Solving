import requests

base_yrl = 'http://localhost:8000/posts/'

while(True):
    requests.get(base_url + 'create/?title=공격!!!&content=공격')
    time.sleep(10000)