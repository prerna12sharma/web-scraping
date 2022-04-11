import json
with open("task5.json","r+")as file:
    data=json.load(file)
    # print(language)
def analayse_movie_language():
    dict={}
    for i in data:
        # print(i)
        if "Language" in i:
            language=i["Language"]
            # print(language)
            if language not in dict:
                dict[language]=1
            else:
                dict[language]+=1 
    
    # print(dict)
    with open("task6.json","w") as file:
        json.dump(dict,file,indent=4)
    return dict
analayse_movie_language()