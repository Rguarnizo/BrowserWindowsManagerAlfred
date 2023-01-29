#!/usr/bin/env python3

import sys
import json
import os

wid,nspace = (sys.argv[1],"".join(sys.argv[2:]))
nspace = nspace.replace(" ","_")

f = open("config.json","r")
data = json.load(f)
f.close()

spaces = data["spaces"]
spaces[nspace]["wid"] = wid;
links = spaces[nspace]["links"];
print(" ".join(links));
