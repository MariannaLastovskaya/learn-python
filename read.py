import json

with open("config.json") as jsonFile:
    data = json.load(jsonFile)
    jsonData = data["Name"]
    print(jsonData)
