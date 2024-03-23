numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))


division=numero1/numero2

if division%2 == 0:
    print("la division es exacta")
    print("cociente: ",int(division))
    print("resto: ",division-int(division))
else :
    print("la division no es exacta")
    print("cociente: ",int (division))
    print("resto: ",division-int(division))