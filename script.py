import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'raleigh' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()

pp.pprint(response)



