import json
with open("task5.json","r+")as file:
    data=json.load(file)
    # print(data)
def analayse_movie_director():
    dict={}
    for i in data:
        if "Director" in i:
            der=i["Director"]
            for j in der:
                for k in j:
                    if k not in dict:
                        dict[k]=1
                    else:
                        dict[k]+=1
    with open("task7.json","w") as file:
        json.dump(dict,file,indent=4)
        return dict
analayse_movie_director() 
            
        
    

