from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json


SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentialsCal.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))


# Abro el archivo con los ids
"""
bufer = open('cargaFinalAtt.json', 'r')
base = json.load(bufer)
bufer.close()
"""

idCalIdEvent = []
miniDict = {
    'calendarId': 'colegioaula21.edu.ar_classroom45b82ce4@group.calendar.google.com',
    'eventId': ''
}
events = GCAL.events().list(calendarId='colegioaula21.edu.ar_classroom45b82ce4@group.calendar.google.com').execute()

print(events)

"""
for i in range(len(base)):
    print(base[i]['calendarId'])
    page_token = None
    while True:
        events = GCAL.events().list(calendarId=base[i]['calendarId'], pageToken=page_token).execute()
        for event in events['items']:
            try:
                if (event['creator']['email'] == 'tics@colegioaula21.edu.ar'):
                    #print(event['creator']['email'])
                    #print(event['id'])
                    miniDict['calendarId'] = base[i]['calendarId']
                    miniDict['eventId'] = event['id']
                    idCalIdEvent.append(miniDict.copy())
                    print(idCalIdEvent)
            except:
                print(event['id'], ' Doent have a crator')
        page_token = events.get('nextPageToken')
        if not page_token:
            break
bufer = open('idCalIdEvent.json', 'w')
bufer.write(json.dumps(idCalIdEvent))
bufer.close()

"""