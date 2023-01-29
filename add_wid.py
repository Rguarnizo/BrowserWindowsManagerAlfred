import sys
import json

query = " ".join(sys.argv[2:])
wid = sys.argv[1]
nspace = query.replace(" ","_")
print(nspace);
print(wid);

f = open("config.json")
data = json.load(f)
f.close()

data["open"][wid] = nspace


f = open("config.json","w");
f.write(json.dumps(data));
f.close()
