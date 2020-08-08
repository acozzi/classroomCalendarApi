import json

bufer = open('cargaFinalAtt.json', 'r')
cargaFinal = json.load(bufer)
bufer.close()

print(cargaFinal[0])