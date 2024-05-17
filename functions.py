import datetime
import json
import os

DATA_FILE = 'timesheet_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def clock_in():
    now = datetime.datetime.now()
    return now

def clock_out():
    now = datetime.datetime.now()
    return now

def calculate_duration(start, end):
    duration = end - start
    return duration