#ejercicio7
km=int(input("kilometraje del auto: "))
COP=(70000+(30000*(km-300)))
masque=150000+(9000*(km-1000))
if (km>300 and km<1000):
    print("debera pagar: ",COP,"COP")
elif (km>=1000):
    print("debera pagar:",masque,"COP")
else:
    print ("debera pagar: 50000 COP")