palabra1=input("ingrese la primera palabra")
palabra2=input("ingrese la segunda palabra")

cantidad1=len(palabra1)
cantidad2=len(palabra2)
resta=len(palabra1)-len(palabra2)

if cantidad1 > cantidad2:
    print(f"la primera palabra tiene {cantidad1} letras y tiene {resta} letras mas que la segunda palabra")
elif cantidad1==cantidad2:
    print("Tienen la misma cantidad de letras")    
else:
    print(f"la segunda palabra tiene {cantidad2} letras y tiene {-resta} letras mas que la primera palabra")