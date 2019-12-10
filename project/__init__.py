import json

def getData(key):
    with open("required_files/classified_data.json", "r") as file:
        return json.load(file)[key]

def updateData(key, value):
    with open('required_files/classified_data.json', 'r') as file:
        data = json.load(file)
        data.update({key : value})
    with open('required_files/classified_data.json', 'w') as file:
        json.dump(data, file, indent=4)
