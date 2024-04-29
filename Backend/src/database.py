import os
import json

DATABASE_FILE = "data.json"


def read_database():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = (
                    []
                )  # Initialize with an empty list if the file is empty or not in JSON format
    else:
        data = []  # Initialize with an empty list if the file doesn't exist
    return data


def write_database(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file)
