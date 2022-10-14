#ejercicio4
monto=int(input("monto total: "))
if monto>5000000:
    invers=monto*0.55
    banco=monto*0.30
    credito=monto*0.15
else:
    invers=monto*0.70
    banco=0
    credito=monto*0.30
interes=credito*0.20
print("la inversion es de: ",invers)
print("prestamo del banco: ",banco)
print("credito a pagar: ",credito)
print("interes por el credito: ",interes)