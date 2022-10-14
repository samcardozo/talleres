#ejercicio14
ante=int(input("lectura anterior: "))
despu=int(input("lectura actual: "))
difer=(despu-ante)
if(difer>=0 and difer<=100):
    kh=4600
elif(difer>=101 and difer<=300):
    kh=80000
elif(difer>=301 and difer<=500):
    kh=100000
elif(difer>=501):
    kh=120000
monto=difer*kh
print("debera pagar: ",monto)