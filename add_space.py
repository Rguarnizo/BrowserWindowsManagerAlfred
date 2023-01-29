import sys
import json

query = " ".join(sys.argv[2:])
wid = sys.argv[1]
nspace = query.replace(" ","_")


f = open("config.json")
data = json.load(f)
f.close()

data["open"][wid] = nspace
spaces = data["spaces"]
spaces[nspace] = {"title":query,"subtitle":query,"arg":nspace,"wid":wid}

f = open("config.json","w");
f.write(json.dumps(data));
f.close()
