import math 
temperaturaOriginalHuevo=float(input("ingrese la temperatura original del huevo: "))

#formula
pi=3.1416
M=47
p=1.038
c=3.7
K= 5.4*(10**-3)

t = ((M**(2/3)) * (c * p)**(1/3)) / (K * pi**2) * ((4 * pi / 3)**(2/3)) * math.log((0.76 * (temperaturaOriginalHuevo - 100) / (70 - temperaturaOriginalHuevo)), math.e)

print("El tiempo estimado es :", t, "segundos")