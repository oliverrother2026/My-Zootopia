import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


animals = load_data("animals_data.json")
print(animals)