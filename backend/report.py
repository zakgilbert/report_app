import requests
import pandas as pd
from BuoyReading import *

def getReport(id):

    url = f'https://www.ndbc.noaa.gov/data/realtime2/{id}.spec'  # Replace with the URL of the file you want to download

    response = requests.get(url)
    buoyReadings = []

    if response.status_code == 200:
        file_object = response.content
        reports = response.text.splitlines()
        cols = reports[0].split()
        colsData = []
        rows = []
        del reports[:2]
        for report in reports:
            rows.append(report.split())

        return {
            "cols": cols,
            "rows": rows
        }

    else:
        return [f'Error: {response.status_code}']
