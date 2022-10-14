#ejercicio1
cantidad=int(input("cantidad invertida: "))
tasa=float(input("tasa de intereses: "))
intereses=cantidad*tasa
total=cantidad+intereses
if intereses > 100000:
    print("la cantidad generada por concepto de intereses: ",intereses,"$ , supera los 100000 $")
else:
    print("la cantidad generada por concepto de intereses: ",intereses,"$ , no supera los 100000 $")
    print ("el total en su cuenta es: ",total)