año=int(input("ingrese el año para saber si es bisisesto: "))

if año%4==0 and año % 100 != 0 or año % 400 == 0:
    print("el año es bisisesto")
else:
    print("el año no es bisisesto")