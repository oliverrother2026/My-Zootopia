import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    if "characteristics" in animal_obj:
        if "diet" in animal_obj["characteristics"]:
            output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal_obj:
        if animal_obj["locations"]:
            output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    if "characteristics" in animal_obj:
        if "lifespan" in animal_obj["characteristics"]:
            output += f'<strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}<br/>\n'

    if "characteristics" in animal_obj:
        if "temperament" in animal_obj["characteristics"]:
            output += f'<strong>Temperament:</strong> {animal_obj["characteristics"]["temperament"]}<br/>\n'

    if "taxonomy" in animal_obj:
        if "scientific_name" in animal_obj["taxonomy"]:
            output += f'<strong>Scientific Name:</strong> {animal_obj["taxonomy"]["scientific_name"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"

    return output


animals_data = load_data("animals_data.json")

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# print(html_template)


output = ""

for animal in animals_data:
    output += serialize_animal(animal)

# print(output)

html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)
