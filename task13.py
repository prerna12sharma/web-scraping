import json
from task4 import movie_details
from task12 import scrape_movie_cast
movie_cast=scrape_movie_cast("https://www.rottentomatoes.com/m/i_lost_my_body")
movie_detail=movie_details("https://www.rottentomatoes.com/m/i_lost_my_body")
list=[]
def movies_details_cast():
    list.append(movie_detail)
    list.append(movie_cast)
    print(list)
    with open("task13.json","w+") as f:
        json.dump(list,f,indent=3)
    return list
movies_details_cast()