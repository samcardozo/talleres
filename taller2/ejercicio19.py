#ejer19
x=int(input("cantidad de naranjas: "))
y=int(input("precio por docena: "))
k=int(input("ingresos por venta del lote: "))
preciouni=y/12
costlot=x*preciouni
porcent=((100*k)/costlot)-100
print("porcentaje de ganancia: ",porcent)