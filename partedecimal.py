#parte decimal de un numero
numero = float(input("ingrese el numero para saber su decimal: "))

numero_decimal = float(numero)-int(numero)

if numero_decimal <= 0:
    numero_decimal = -numero_decimal
    
print (numero_decimal)
