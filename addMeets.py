import json
import csv

# Openning JSON into RAM
buf = open('aulasAtt.json', 'r')
aulas = json.load(buf)
buf.close

def mergeData(ubicacion,link):
    aulas[ubicacion]['meet'] = link

def findSeq(valorId):
    for i in range(len(aulas)):
        if (aulas[i]['id'] == valorId):
            return i

# Open CSV into RAM

with open('idMeet.csv') as meet:
    arregloCSV = csv.reader(meet, delimiter=',')

    for row in arregloCSV:
        ubica = findSeq(row[0])
        mergeData(ubica,row[1])


buffer = open('./aulasAttMeet.json', 'w')
buffer.write(json.dumps(aulas))
buffer.close()