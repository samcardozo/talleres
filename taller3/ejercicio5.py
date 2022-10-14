#ejercicio5
importe1=int(input("importe global de las ventas departamento 1: "))
importe2=int(input("importe global de las ventas departamento 2: "))
importe3=int(input("importe global de las ventas departamento 3: "))
salario=int(input("salario en bruto: "))
ventas=int(input("importe individual de las ventas: "))
importe=importe1+importe2+importe3
necesity=importe*0.33
extraporcent=salario*0.20
salarioextra=salario+(extraporcent)
if ventas>necesity:
    print("recibira: ",salarioextra)
else:
    print("recibira: ",salario)