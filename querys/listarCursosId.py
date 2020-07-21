import json
bufer = open('files/aulas.json', 'r')
aulasJ = json.load(bufer)
bufer.close()


aulas = []
for i in range(len(aulasJ)):
    aula = {
        "id": aulasJ[i]['id'],
        "descripcion":aulasJ[i]['descriptionHeading']
    }
    aulas.append(aula)

lista = open('files/listadoIds.json','w')
lista.write(json.dumps(aulas))
lista.close()