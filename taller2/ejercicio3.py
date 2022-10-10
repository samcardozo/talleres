#ejer3
sueldo=int(input("ingrese sueldo base= "))
venta1=int(input("ingrese valor de la venta 1: "))
venta2=int(input("ingrese valor de la venta 2: "))
venta3=int(input("ingrese valor de la venta 3: "))
comision= (venta1+venta2+venta3)*0.10
print("ganancia por comisiones: ", comision)
suelcom= sueldo+comision
print("ganancia total: ", suelcom)