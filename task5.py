import json
from task1 import scrap_list
from task4 import movie_details
all_movie=scrap_list()
# print(all_movie)
def get_movie_details_list():
    list1=[]
    for i in all_movie:
       k=i["link"]
    #    print(k)
       d=movie_details(k)
       list1.append(d)
    #    print(list1)
    with open("task5.json","w") as file:
        json.dump(list1,file,indent=4)
    return list1
get_movie_details_list()
        