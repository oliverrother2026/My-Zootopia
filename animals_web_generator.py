import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


animals_data = load_data("animals_data.json")

for animal in animals_data:
    print("Name:", animal["name"])

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            print("Diet:", animal["characteristics"]["diet"])

    if "locations" in animal:
        if animal["locations"]:
            print("Location:", animal["locations"][0])

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            print("Type:", animal["characteristics"]["type"])

    print()