import json
with open("task5.json","r") as b:
   movies= json.load(b)
def analyse_language_and_directors():
    dic={}
    director_list=[]
    for i in movies:
        for j in i["Director"]:
            if j not in director_list:
                director_list.append(j)
    for i in director_list:
        d={}
        for j in movies:
            if i in j["Director"]:
                for k in i:
                    if "Language" in j:
                        a=j["Language"]
                        if a in d:
                            d[a]=d[a]+1                        
                        if a not in d:
                            d[a]=1 
                dic[k]=d
        # print(dic)
        with open("task10.json","w") as f:
            json.dump(dic,f,indent=4)
analyse_language_and_directors()      