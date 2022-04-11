from bs4 import BeautifulSoup
import requests
import json
url=("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
page=requests.get(url)
# htmlcontent=page.htmlcontent
# print(htmlcontent)
soup=BeautifulSoup(page.text,"html.parser")
def scrap_list():
    list=[]
    main_div=soup.find('div',class_="body_main container")
    table=main_div.find('table',class_="table")
    trs=table.find_all('tr')
    # print(trs)
    for i in trs:
        d1={}
        tds=i.find_all('td')
        for j in tds:
            rank=i.find('td',class_="bold").get_text() [:-1]
            d1["rank"]=int(rank)
            name=i.find("a",class_="unstyled articleLink")["href"][3:] 
            d1["name"]=name
            link=i.find("a",class_="unstyled articleLink")["href"]
            m="https://www.rottentomatoes.com"+link
            d1["link"]=m
            year=i.find("a",class_="unstyled articleLink").get_text()
            year1=year.strip()
            # print(year1)
            d1["year"]=int(year[-5:-1])
            # print(d1)
        list.append(d1)
    #print(list)
    if {} in list:
        list.remove({})
        # print(list)
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
movie_data=scrap_list()