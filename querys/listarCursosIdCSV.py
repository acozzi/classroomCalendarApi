import json
import csv
bufer = open('files/parsed.json', 'r')
aulasJ = json.load(bufer)
bufer.close()


with open('files/classrooms.csv', mode='w') as cf:
    cf = csv.writer(cf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(aulasJ)):
        aula = aulasJ[i]['id'] + ',' + aulasJ[i]["name"] + ',' + aulasJ[i]['descriptionHeading'] + ',' + aulasJ[i]["enrollmentCode"] + ',' + aulasJ[i]["alternateLink"] + ',' + aulasJ[i]["calendarId"] + ',' + aulasJ[i]["name"]
        cf.writerow([aula])
"""
i = 0
aula = aulasJ[i]['id'] + ',' + aulasJ[i]["name"] + ',' + aulasJ[i]['descriptionHeading'] + ',' + aulasJ[i]["enrollmentCode"] + ',' + aulasJ[i]["alternateLink"] + ',' + aulasJ[i]["calendarId"] + ',' + aulasJ[i]["name"]
print(aula)
"""