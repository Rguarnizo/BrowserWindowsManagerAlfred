import sys
import json

wid = sys.argv[1]
links = sys.argv[3::2]
print(links)
print(wid)

f = open("config.json","r")
data = json.load(f)
f.close()

nspace = data["open"][wid]
del data["open"][wid]

spaces = data["spaces"]
spaces[nspace]["links"] = links;

f = open("config.json","w");
f.write(json.dumps(data));
f.close()
