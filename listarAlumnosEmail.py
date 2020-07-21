from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly','https://www.googleapis.com/auth/classroom.rosters','https://www.googleapis.com/auth/classroom.profile.emails']

def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    bufer = open('./aulas.json', 'r')
    aulas = json.load(bufer)
    bufer.close()

    for i in range(len(aulas)):
        courseId = aulas[i]['id']
        results = service.courses().students().list(courseId=courseId).execute()
        resultsD = service.courses().teachers().list(courseId=courseId).execute()
        alumnos = results.get('students', [])
        docentes = resultsD.get('teachers', [])
        
        attendersEmail = []
        for j in range(len(docentes)):
            attendersEmail.append(docentes[j]['profile']['emailAddress'])
        
        for j in range(len(alumnos)):
            attendersEmail.append(alumnos[j]['profile']['emailAddress'])
        
        aulas[i]['attenders'] = attendersEmail
        print(i)
       
        
    buffer = open('./aulasAtt.json','w')
    buffer.write(json.dumps(aulas))
    buffer.close()
if __name__ == '__main__':
    main()