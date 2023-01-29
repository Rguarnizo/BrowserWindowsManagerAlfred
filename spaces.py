import sys
import json

f = open("./config.json","r")

data = json.load(f)

print(json.dumps({"items":[value for key,value in data['spaces'].items()]}))

f.close()
