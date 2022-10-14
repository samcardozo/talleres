#ejercicio2
sueldo=int(input("sueldo del trabajador: "))
a15=(sueldo*0.15)+sueldo
a12=(sueldo*0.12)+sueldo
if sueldo < 900000:
    print("nuevo saldo: ",a15, "COP")
else:
    print("nuevo saldo: ",a12, "COP")