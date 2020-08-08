from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json

bufer = open('cargaFinalAtt.json', 'r')
#bufer = open('prueba.json', 'r')
eventos = json.load(bufer)
bufer.close()


SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentialsCal.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

eventosCreados = []

for i in range(len(eventos)):
    e = GCAL.events().insert(calendarId=eventos[i]['calendarId'],
            sendNotifications=True, body=eventos[i]['event']).execute()
    eventos.append(e)

bufer = open('eventos.json', 'w')
bufer.write(json.dumps(eventosCreados))
bufer.close()