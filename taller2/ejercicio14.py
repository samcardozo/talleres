#ejer14
lecant=int(input("lectura anterior: "))
lecact=int(input("lectura actual: "))
leckv=int(input("costo por kilovatio: "))
consumo=lecact-lecant
montot=consumo*leckv
print("monto total a pagar en un mes: ", montot)