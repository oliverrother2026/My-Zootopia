import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


animals_data = load_data("animals_data.json")

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

#print(html_template)


output = ""

for animal in animals_data:
    output += f"Name: {animal['name']}\n"

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"

    if "locations" in animal:
        if animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"

    output += "\n"

#print(output)

html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)