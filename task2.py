from task1 import movie_data
import json
data=open('task1.json')
movies=json.load(data)
def group(movies):
    dict1={}
    for i in movies:
        main=[]
        year=i['year']
        if year not in dict1:
            for k in movies:
                if year==k['year']:
                    main.append(k)
            dict1[year]=main
    with open('task2.json','w+') as file:
        json.dump(dict1,file,indent=4)
        a=json.dumps(dict1)
year1=group(movies)