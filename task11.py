import json
with open("task5.json","r") as file:
    list=json.load(file)
def analyse_movies_genre():
    dict={}
    for i in list:
        if "Genre" in i:
            genre=i["Genre"]
        # print(genre)
            for k in genre:
                # print(k)
                if k not in dict:
                    dict[k]=1
                else:
                    dict[k]+=1
        with open("task11.json","w")as f:
            json.dump(dict,f,indent = 4)
analyse_movies_genre()