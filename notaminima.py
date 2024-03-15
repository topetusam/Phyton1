nota_certamen1= int(input("Ingrese la nota del certamen 1: "))
nota_certamen2= int(input("Ingrese la nota del certamen 2: "))
nota_laboratorio= int(input("Ingrese la nota del laboratorio: "))

#nota final = 60
Nota_final = 60
nota_promedio= (Nota_final-nota_laboratorio*0.3)/0.7   

nota_certamen3=(3*nota_promedio)-nota_certamen1-nota_certamen2

print (nota_certamen3)
