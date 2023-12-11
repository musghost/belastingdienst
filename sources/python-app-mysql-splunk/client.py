import requests
from time import sleep
from random import random, seed, randint

seed(1)
url = 'http://greeting-app:5000/greet'
x=1

def pythonrequests():
    country_map = ('Amsterdam', 'New York', 'Berlin', 'London')
    payload = {
        'name': 'Andres',
        'age': 23,
        'city': country_map[randint(0, 3)],
    }
    try:
        r=requests.post(url, data=payload)
    #   print('posting: ', r.url, ' ', r.text)
    except requests.exceptions.RequestException as err:
        print(err)

while x:
    pythonrequests()
    y = random()
    # print('Sleeping: ', round(y,2))
    sleep(round(y,2))