import json

bufer = open('cargaFinal.json', 'r')
cargaFinal = json.load(bufer)
bufer.close()

bufer = open('aulasAtt.json', 'r')
aulasAtt = json.load(bufer)
bufer.close()



def encontrarAttenders(idAulaEvento):
    for i in range(len(aulasAtt)):
        if (idAulaEvento == aulasAtt[i]['id']):
            return aulasAtt[i]['attenders']
    print('No hubo coindicdencia ', idAulaEvento)


listaMails = encontrarAttenders("72358360930")
def listToDict(lista):
    listaDicts = []
    for email in lista:
        listaDicts.append({"email": email})
    return listaDicts


for i in range(len(cargaFinal)):
    attendees = encontrarAttenders(cargaFinal[i]['classroomId'])
    cargaFinal[i]['event']['attendees'] = listToDict(attendees)



bufer = open('cargaFinalAtt.json', 'w')
bufer.write(json.dumps(cargaFinal))
bufer.close()
