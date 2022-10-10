#ejer15
precfin=int(input("precio final pagado por un producto: "))
precvent=int(input("precio de venta al publico: "))
pagoext=precvent-precfin
pda=(pagoext*100)/precvent
print("porcentaje de descuento aplicado: ", pda)