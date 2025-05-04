lista=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
dicionario={}
for i in lista:
    dicionario.update({i:lista.count(i)})
print(dicionario)