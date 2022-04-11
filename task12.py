import requests
import json
from bs4 import BeautifulSoup
def scrape_movie_cast(link):
    url=requests.get(link)
    soup=BeautifulSoup(url.text,"html.parser")
    main_div=soup.find('div',class_="castSection")
    castDiv=main_div.find_all("div",class_="media-body")
    dic={}
    dic1={}
    list=[]
    for i in castDiv:
        M=i.span.text
        N=M.split()
        X=N[0].replace(",","").strip()
        Y=" "
        k= N[1].replace(",","").strip()
        Z=X+Y+k
        list.append(Z)
    dic["Cast_Name"]=list
    # print(dic)
    with open("task12.json","w+") as f:
        json.dump(dic,f,indent=3)
    return dic
scrape_movie_cast("https://www.rottentomatoes.com/m/i_lost_my_body")


    



