import json
import requests
with open("task2.json","r+") as file:
    data=json.load(file)
def decate(data):
    list=[]
    dict={}
    for m in data:
        a=int(m)
        mod=a%10
        dec=a-mod
        # print(dec)
        if dec not in list:
            list.append(dec)
            # print(list)
    list.sort()
    # print(list) 
    for j in list:
        dict[j]=[]
        # print(j)
        dic1=j+9
        for k in data:
            if int(k)<=dic1 and int(k)>=j:
                for l in data[k]:
                    dict[j].append(l)
                with open("task3.json","w+") as file:
                    json.dump(dict,file,indent=4)
                    # b=json.dumps(dict)
    return dict
(decate(data))

