
import json

with open("config.json") as jsonFile:
     data = json.load(jsonFile)
     jsonData = data["emp_details"]
     for x in jsonData:
          keys = x.keys()
          print(keys)
          values = x.values()
          print(values)