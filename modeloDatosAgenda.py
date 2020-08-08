import json
import csv

mokup = {
    "classroomId": 0,
    "calendarId": "",
    "event": {}
}
event = {
    "summary": "",
    "description": "",
    "location": "",
    "start": {},
    "end": {},
    "recurrence": [
    ],
    "attendees": [
    ],
    "guestsCanInviteOthers": False,
    "reminders": {
        "useDefault": False,
        "overrides": [
            {
            "method": "popup",
            "minutes": 10
            },
            {
            "method": "email",
            "minutes": 60
            }
        ]
    }
}
start = {
        "dateTime": "",
        "timeZone": "America/Argentina/Buenos_Aires"
    }
end =  {
        "dateTime": "",
        "timeZone": "America/Argentina/Buenos_Aires"
    }
cargaList = []

def loadData(data):
    cargaList.append(data.copy())
  

#classroomId[0],summary[1],classroomLink[2],calendarId[3]
#start      [4],end    [5],   recurrence[6]
with open('agenda.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mokup['classroomId'] = row[0]
        mokup['calendarId'] = row[3]
        event['summary'] = row[1]
        event['description'] = 'Acceder al Meet Link desde el classroom: ' + row[2]
        event['location'] = row[2]
        event['recurrence'] = [row[6]]
        start['dateTime'] = row[4]
        end['dateTime'] = row[5]
        event['start'] = start.copy()
        event['end'] = end.copy()
        mokup['event'] = event.copy()
        loadData(mokup)



 


bufer = open('cargaFinal.json', 'w')
bufer.write(json.dumps(cargaList))
bufer.close()
