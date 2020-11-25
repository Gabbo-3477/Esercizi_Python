print("Calcolo media stipendio")
stipendi = []
while True:
    stipendio = int(input("Quant'è lo stipendio? "))
    if stipendio == -1:
        break
    else:
        stipendi.append(stipendio)
totstipendi = len(stipendi)
sumstipendi = sum(stipendi)
media = sumstipendi/sumstipendi
print("Questa è la media di tutti gli stipendi : ", media, "€")