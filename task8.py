import json
import os
import requests
with open("task1.json","r+") as file:
        a=json.load(file)
def text():
    for i in a:
        path="/home/admin123/Desktop/web scrapping/movie.text"+i["name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/web scrapping/movie.text"+i["name"]+".text","w")
            url=requests.get(i["link"])
            create1=create.write(url.text)
            create.close()
text()
        
