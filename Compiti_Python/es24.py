voti1=int(input("Inserire voti di Buglione:"))
voti2=int(input("Inserire voti di Righetti:"))
votitotali=voti1+voti2
percentualevoto1=voti1*100
percentualevoto2=percentualevoto1/votitotali
percentualevoto3=voti2*100
percentualevoto4=percentualevoto3/votitotali
if percentualevoto2>percentualevoto4:
    print("Il rappresentante è Buglione!")
elif percentualevoto4>percentualevoto2:  
    print("Il rappresentate è Righetti!")
else:
    print("Sono entrambi rappresentanti!")