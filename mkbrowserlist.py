#!/usr/bin/python
import os
import markdown
page = "# Page List\n\n"
for item in sorted(os.listdir("pages")):
    if item.endswith(".md"):
        item = item.replace(".md","")
        pagelet = "* [about:{}](about:{})\n".format(item, item)
        page += pagelet
page = markdown.markdown(page)        
with open("pages/list.md","w") as f:
    f.write(page)
print("Successfully written about:list")