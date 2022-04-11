# from bs4 import BeautifulSoup
# import requests
# import json
# url=("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
# page=requests.get(url)
# # print(page)
# s=BeautifulSoup(page.text,"html.parser")
# # print(s)
# def scrap_list():
#     list=[]
#     main_div=s.find("div",class_="body main container")
#     table=main_div.find("table",class_="table")
#     trs=table.find_all("tr")
#     for i in trs:
#        d1={}
#        tds=i.find_all("td")
#        rank=i.find("td",class_="bold").get_text()[:-1]
#        d1[rank]=int(rank)
#        print(d1)
# scrap_list()
# import json
# import requests
# with open("task2.json","r+") as file:
#     data=json.load(file)
# def decate(data):
#     dic={}
#     list=[]
#     for m in data:
#         # print(m)
#         a=int(m)
#         mod=a%10
#         dec=a-mod
    #     print(dec)
    #     if dec not in list:
    #         list.append(dec)
    #         print(list)
            
    # list.sort()
    # print(list)
    # for j in list:
    #     dic[j]=[]
    # for j in dic:
    #     print(j)
    #     dic1=j+9
    #     for k in data:
    #         if int(k)<=dic1 and int(k)>=j:
#                 for l in data[k]:
#                     dic[j].append(l)
#                 with open("task3.json","w+") as file:
#                     json.dump(dic,file,indent=4)
#                     b=json.dumps(dic)
#     return dic
# print(decate(data))
    
# n=int(input("enter num"))
# if n>2 and n<5:
#     if n%2==0:
#         print("Not Weird")
#     else:
#         print("Weird")
# elif n>6 and n<20:
#     if n%2==0:
#         print("Weird")
#     else:
#         print("Not Weird")
# elif n>20:
#     if n%2==0:
#         print("Not Weird")
#     else:
#         print("Weird")
# else:
#     print("Nothing")      
       
# b=a.split()
# print(b)
# list=[]
# list.append(1) 
# list.append(2)
# list.insert(1,3) 
# print(list)  
# a=7
# b=5
# c="nikki"
# d=a*b
# f=d-b
# print(c)
# a="prerna"
# b="shivi"
# c=a+b
# print(c)
# a="priya"
# b=7
# c=a*7
# print(c)
# print(type(c))
# a="sam"
# b="7.2"
# c="12"
# d=float(b)
# e=int(d)
# print(a+c+str(e))
# a="ujalaneha"
# print(a[2:9])

# interchanging

# a=10
# b=8
# (a,b)=(b,a)
# print(a,b)

# temporary
# a=10
# b=8
# c=a
# a=b
# b=c
# print(a,b)

# a="prerna"
# b ="sharma"
# c=232
# d=1.4
# e=c+d
# f=str(e)+a+b
# print(f)

# num=[1,2,3,4]
# sum=0
# sum=num[0]+num[1]
# print(sum)

list1=[2,4,3]
list2=[5,6,4]
list=[]
sum=0
for i in list1:
    # print(i)
    for j in list2:
        sum=i+j
        list.append(sum)
    print(sum)