from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses','https://www.googleapis.com/auth/classroom.courses.readonly']

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
    course_id = '61991289262'
    try:
        course = service.courses().get(id=course_id).execute()
        print(course)
        #print(u'Course "{0}" found.'.format(course.get('name')))

    except errors.HttpError as e:
        error = simplejson.loads(e.content).get('error')
        if(error.get('code') == 404):
            print(u'Course with ID "{0}" not found.'.format(course_id))
        else:
            raise




    #course = service.courses().get(courseId='61991289262').execute()
    #print(type(course))
if __name__ == '__main__':
    main()