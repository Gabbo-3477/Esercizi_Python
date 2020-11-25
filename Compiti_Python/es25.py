candidato1 = input("Chi è il primo candidato? ")
voti1 = int(input("Quanti voti ha raccolto il primo candidato?"))
candidato2 = input("Chi è il secondo candidato? ")
voti2 = int(input("Quanti voti ha raccolto il secondo candidato ?"))
candidati = [candidato1, candidato2]
candidati.sort()
print(candidati)
if voti1 < voti2:
    print(candidato2, candidato1)
elif voti2 < voti1:
    print(candidato1, candidato2)
