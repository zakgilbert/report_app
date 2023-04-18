import requests
import pandas as pd
from BuoyReading import *

url = 'https://www.ndbc.noaa.gov/data/realtime2/51101.spec'  # Replace with the URL of the file you want to download

response = requests.get(url)
buoyReadings = []

if response.status_code == 200:
    file_object = response.content
    reports = response.text.splitlines()
    cols = reports[0].split()
    colsData = []
    del reports[:2]
    for report in reports:
        report = report.split()
        buoyReading = BuoyReading(report)
        buoyReading.setData()
        buoyReadings.append(buoyReading)
    for reading in buoyReadings:
        colsData.append(reading.getData())
    df = pd.DataFrame(colsData, columns=cols)
    print(df.to_string())

else:
    print(f'Error: {response.status_code}')
