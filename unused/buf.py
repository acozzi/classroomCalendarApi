
token      = "11~asdfghjkl"
api        = "https://x.instructure.com/api/v1/"
headers    = {'Authorization' : 'Bearer ' + '%s' % token}

course_id = 123
payload = {
     'enrollment_role':'StudentEnrollment',
     'per_page':100
}
url = api + 'courses/'+ str(course_id) +'/users'
results = requests.get(url, params = payload, headers = headers)
response = results.text
users = json.loads(response)
print(users)

# headers in case you need to deal with pagination
headers = results.headers
print(headers)



"""
    website: https://www.buenosaires.gob.ar/desarrollourbano/transporte/apitransporte/api-doc
"""

import requests
import json

# Variables
url="https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus"
aut = {
    'client_id':"b05ee44f5ddd414dad71815064295290",
    'client_secret':"c28337fb1C964e6FAe37b2AC0028d222" 
}

# Funciones
def imprimeOrdenado(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get(url,aut)
print(response.status_code)
estaciones = response.json()['data']
print(estaciones.get('stations'))

print(estaciones.get('stations')[0])
for i in range(len(estaciones.get('stations'))):
    print(estaciones.get('stations')[i].get('station_id'))


