#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
horaActual=int(input("ingrese la hora actual :"))
horaFutura=int(input("ingrese cuantas horas desea adelantar a su reloj :"))


hora=(horaActual+horaFutura)%12

print(f"la nueva hora es {hora}:")


