#ejercicio9
nombre=input("nombre: ")
monto=int(input("monto: "))
if (monto<50000):
    print(nombre)
    print("su monto es: ",monto)
    print("no se aplica descuento")
    print("debera pagar: ",monto)
elif (monto>=50000 and monto<=100000):
    print(nombre)
    print("su monto es: ",monto)
    print("se aplica un descuento del 5%")
    d5=monto-(monto*0.05)
    print("debera pagar: ",d5)
elif (monto>100000 and monto<=700000):
    print(nombre)
    print("su monto es: ",monto)
    print("se aplica un descuento del 11%")
    d11=monto-(monto*0.11)
    print("debera pagar: ",d11)
elif (monto>700000 and monto<=1500000):
    print(nombre)
    print("su monto es: ",monto)
    print("se aplica un descuento del 18%")
    d18=monto-(monto*0.18)
    print("debera pagar: ",d18)
else:
    print(nombre)
    print("su monto es: ",monto)
    print("se aplica un descuento del 25%")
    d25=monto-(monto*0.25)
    print("debera pagar: ",d25)