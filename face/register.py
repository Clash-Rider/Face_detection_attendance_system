import json
import time

namesArr=[]
interval=10

def jsonregister(names_detected):

    timenow=time.time()

    with open('info.json','r') as file:
        data=json.load(file)

    for i in names_detected:
        for j in data:
            namesArr.append(j["name"])
            if (i == j["name"] and (j["date"]+interval)<timenow):
                j['atten']+=1
                j["date"]=timenow

    with open('info.json','w') as outfile:
        json.dump(data,outfile)

    for i in names_detected:
        if (i not in namesArr):
            data.append({"name":i, "atten":1, "date":timenow, "image":(f"data/{i}_0.jpg") })
        else:
            return
    with open('info.json','w') as outfile:
        json.dump(data,outfile)