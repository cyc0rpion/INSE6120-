#fetchHashes.py
#Author: Mohit Balu (mohit.balu@mail.concordia.ca)
#Desc: Python script to convert MobSF JSON reports to XLSX files, for the fulfilment of academic project of INSE6120.

import requests
import os

auth="2028def2c5f09d7370d5f7c196717b3a63ad755e412aea71b7cc2f921ec7da80"

headers1 = {'Authorization': auth}

r1 = requests.get('http://localhost:8000/api/v1/scans?page=1&page_size=100', headers=headers1)

data = r1.json()
content = data['content']

filenames=[]
hashes=[]
names=[]

for each in content:
    name = each['APP_NAME']
    ext = each['SCAN_TYPE']
    identity = each['MD5']

    #print(identity)

    names.append(name)

    postdata = "hash="+str(identity)
    filename = "Report_"+str(name)+"_"+str(ext)+".json"

    filename = filename.replace(' ','')
    filename = filename.replace('&','')

    filenames.append(filename)
    hashes.append(postdata)


#print(filenames)
#print("\n\n")
#print(hashes)

print("\nTotal reports = ",len(hashes))
count=1
if(len(filenames) == len(hashes)):
    for i in range(len(filenames)):
        command = 'curl -s -X POST --url http://localhost:8000/api/v1/report_json --data '+hashes[i]+' -H "Authorization: '+auth+'"'

        os.system(command+" > "+filenames[i])


        print(str(count)+". "+names[i]+"'s report is at "+filenames[i])
        count+=1

