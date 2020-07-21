from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentialsCal.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-03:00'  # PDT/MST/GMT-7
#6/8/2020T9:45:00
EVENT = {
    'summary': 'Titulo de la reunion',
    'start':  {'dateTime': '2020-07-20T19:00:00%s' % GMT_OFF},
    'end':    {'dateTime': '2020-07-20T22:00:00%s' % GMT_OFF},
    'attendees': [
        {'email': 'acozzi@colegioaula21.edu.ar'},
        {'email': 'jperez@colegioaula21.edu.ar'},
    ],
}
EVENT_Created = {
    "summary": "Reunion de Prueba",
    "description": "Body de la descripción href=\"https://meet.google.com/vka-cgir-udh\" ",
    "location": "href=\"https://meet.google.com/vka-cgir-udh\"",
    "start": {
        "dateTime": "2020-07-20T19:00:00-03:00",
        "timeZone": "America/Argentina/Buenos_Aires"
    },
    "end": {
        "dateTime": "2020-07-20T22:00:00-03:00",
        "timeZone": "America/Argentina/Buenos_Aires"
    },
    "recurrence": [
    "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO"
    ],
    "attendees": [
        {"email": "acozzi@colegioaula21.edu.ar"},
        {"email": "jperez@colegioaula21.edu.ar"},
        {"email": "tics@colegioaula21.edu.ar"}
    ],
    "guestsCanInviteOthers": false,
    "reminders": {
        "useDefault": false,
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

e = GCAL.events().insert(calendarId='c_kim6g9cg9paf4drf399rh5n3qg@group.calendar.google.com',
        sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))