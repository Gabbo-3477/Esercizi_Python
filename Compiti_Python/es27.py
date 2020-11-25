print("Calcolo veicoli transitati")
veicoli = []
while True:
    transito = int(input("Quanti veicoli sono transitati oggi? "))
    if transito == 0:
        break
    else:
        veicoli.append(transito)
veicolitotali = sum(veicoli)
print("Questi sono i veicoli transitati in totale: ", veicolitotali)