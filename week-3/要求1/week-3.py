import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as datalist:
  data=json.load(datalist)
resultlist=data["result"]["results"]
spot_list=[]

for i in range(0,len(resultlist)):
  addresslist=list(resultlist[i]["address"]) 
  regionname_split=resultlist[i]["address"].split("區") 
  regionname=regionname_split[0][-2]+regionname_split[0][-1]+"區" 
  
  photo_split=resultlist[i]["file"].split("https://") 
  photo="https://"+photo_split[1] 

  spot_dic={}
  spot_dic['stitle']=resultlist[i]['stitle']
  spot_dic['region']=regionname
  spot_dic['longitude']=resultlist[i]['longitude']
  spot_dic['latitude']=resultlist[i]['latitude']
  spot_dic['file']=photo
  spot_list.append(spot_dic)

import csv
with open('data.csv','w') as csvfile:
  objects=['stitle','region','longitude','latitude','file'] 
  writer=csv.DictWriter(csvfile,fieldnames=objects)
  writer.writerows(spot_list)
