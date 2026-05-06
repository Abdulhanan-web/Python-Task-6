import csv
import json

def input_data():
    data = []
    n = int(input("Enter number of records: "))

    for _ in range(n):
        record = {
            "name": input("Name: "),
            "id": input("ID: "),
            "email": input("Email: "),
            "role": input("Course/Role: "),
            "performance": input("Performance/Details: ")
        }
        data.append(record)

    return data


def load_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print("Error loading CSV:", e)
    return data


def load_json(file_path):
    try:
        with open(file_path) as file:
            return json.load(file)
    except Exception as e:
        print("Error loading JSON:", e)
        return []