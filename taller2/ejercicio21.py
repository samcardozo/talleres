#ejer21
contado=int(input("precio por compra al contado: "))
t=int(input("precio por cuota: "))
t12=t*12
diferencia=contado-t12
porcentaje=(((diferencia*100)/contado)*2)*(1/2)
print("porcentaje: ",porcentaje)