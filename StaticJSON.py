#staticJSON.py
#Author: Mohit Balu (mohit.balu@mail.concordia.ca)
#Desc: Python script to fetch json reports from MobSF, for the fulfilment of academic project of INSE6120.

#!/usr/bin/python3

import os
import json
import xlsxwriter


workbook = xlsxwriter.Workbook("/shared/Android Security/SecurityAnalysis.xlsx")

worksheet1 = workbook.add_worksheet("App Data")

worksheet1.write('A1','#')
worksheet1.write('B1','App Name')
worksheet1.write('C1','App Version')
worksheet1.write('D1','Hash')
worksheet1.write('E1','Security Score')
worksheet1.write('F1','Package Name')

worksheet2 = workbook.add_worksheet("Permissions")

worksheet2.write('A1','#')
worksheet2.write('B1','App Name')
worksheet2.write('C1','Permission Activity')
worksheet2.write('D1','Severity')
worksheet2.write('E1','Information')
worksheet2.write('F1','Description')

worksheet3 = workbook.add_worksheet("Trackers")

worksheet3.write('A1','#')
worksheet3.write('B1','App Name')
worksheet3.write('C1','Tracker Name')
worksheet3.write('D1','Category')
worksheet3.write('E1','URL')


files = os.listdir("./JSONReports")

count=1
i=2
j=2
k=2

for candidate in files:
    file = open("./JSONReports/"+candidate)
    data = json.load(file)
    #print("App Name: "+data['app'])

    # AppData Start

    #print("App Name: "+data['app_name'])
    #print("App Version: "+data['version'])
    #print("Package Name: "+data['package_name'])
    appsec = data['appsec']
    #print("Security Score: "+str(appsec['security_score']))
    #print("Hash: "+str(appsec['hash']))


        #print(perm+", "+permissions[perm]['status']+", "+permissions[perm]['info']+", "+permissions[perm]['description'])
    worksheet1.write("A"+str(i),i-1)
    worksheet1.write("B"+str(i),str(data['app_name']))
    worksheet1.write("C"+str(i),str(data['version']))
    worksheet1.write("D"+str(i),str(appsec['hash']))
    worksheet1.write("E"+str(i),int(appsec['security_score']))
    worksheet1.write("F"+str(i),str(data['package_name']))
    i+=1
    count+=1

    # AppData Ends


    # Permissions Start

    permissions = data['permissions']

    #print("\nPermissions\n")

    for perm in permissions:
        #print(perm+", "+permissions[perm]['status']+", "+permissions[perm]['info']+", "+permissions[perm]['description'])
        worksheet2.write("A"+str(j),j-1)
        worksheet2.write("B"+str(j),str(data['app_name']))
        worksheet2.write("C"+str(j),str(perm))
        worksheet2.write("D"+str(j),str(permissions[perm]['status']))
        worksheet2.write("E"+str(j),str(permissions[perm]['info']))
        worksheet2.write("F"+str(j),str(permissions[perm]['description']))
        j+=1
        count+=1

    # Permissions End



    # Trackers Start

    #print("\nTrackers\n")



    trackers = data['trackers']
    detectedTrackers = int(trackers['detected_trackers'])
    eachTracker = trackers['trackers']

    #print("Tracker Name, Category, URL")

    for each in eachTracker:
        #print(perm+", "+permissions[perm]['status']+", "+permissions[perm]['info']+", "+permissions[perm]['description'])
        worksheet3.write("A"+str(k),k-1)
        worksheet3.write("B"+str(k),str(data['app_name']))
        worksheet3.write("C"+str(k),str(each['name']))
        worksheet3.write("D"+str(k),str(each['categories']))
        worksheet3.write("E"+str(k),str(each['url']))
        k+=1
        count+=1


    #for each in eachTracker:
        #print(each['name']+", "+each['categories']+", "+each['url'])

    # Trackers End

workbook.close()



