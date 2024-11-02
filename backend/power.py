import requests
import pandas as pd
from BuoyReading import *
from util import *
import datetime

def getSwellPower(id):
    url = f'https://www.ndbc.noaa.gov/data/5day2/{id}_5day.spectral'

    response = requests.get(url)
    print(response.text)

    return response.text