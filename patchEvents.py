from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json

def replace(old):
    new = old.replace('Â', '')
    new = new.replace('Ã', 'í') 
    new = new.replace('í ³', 'ó')
    new = new.replace('íº', 'ú')
    new = new.replace('í¡', 'á')
    new = new.replace('í‰', 'é')
    return new

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentialsCal.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))



# Abro el archivo con los ids
bufer = open('idCalIdEvent.json', 'r')
base = json.load(bufer)
bufer.close()
"""
event = GCAL.events().get(calendarId=base[2]['calendarId'], eventId=base[2]['eventId']).execute()
print(event['summary'])
"""
# First retrieve the event from the API.


for i in range(len(base)):
    event = GCAL.events().get(calendarId=base[i]['calendarId'], eventId=base[i]['eventId']).execute()
    summaryOld = event['summary']
    summaryNew = replace(summaryOld)
    event['summary'] = summaryNew
    updated_event = GCAL.events().update(calendarId=base[i]['calendarId'], eventId=base[i]['eventId'], body=event).execute()
    print(updated_event['updated'])
    print(event['summary'])
#event['summary'] = 'Appointment at Somewhere'



#updated_event = GCAL.events().update(calendarId='colegioaula21.edu.ar_classroom45b82ce4@group.calendar.google.com', eventId='5gk9dhshikap5krha8npn8s3vo', body=event).execute()

# Print the updated date.
#print(updated_event['updated'])





#eventPatch = GCAL.events().patch(calendarId='colegioaula21.edu.ar_classroom45b82ce4@group.calendar.google.com', eventId='5gk9dhshikap5krha8npn8s3vo')



#event = GCAL.events().get(calendarId='colegioaula21.edu.ar_classroom45b82ce4@group.calendar.google.com', eventId='5gk9dhshikap5krha8npn8s3vo').execute()
#print(event['summary'])
