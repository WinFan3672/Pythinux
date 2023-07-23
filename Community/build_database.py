#!/usr/bin/python
import os
db = {}
for item in os.listdir():
    if os.path.isdir(item):
        ## Check for contents
        if "package.szip3" in os.listdir(item) and "package.info" in os.listdir(item):
            url_base = ""
            with open(f"{item}/package.info") as f:
                g = f.read().split("|")
                if len(g) != 2:
                    print("Invalid package info.")
                    continue
            dic = {"name":g[0],
                "url":url_base,
                "desc":g[1],
                }
            db[item] = dic
        else:
            continue
print(db)        