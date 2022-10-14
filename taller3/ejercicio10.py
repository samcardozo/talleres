#ejercicio10
cate=int(input("su categoria: "))
sueldo=int(input("sueldo bruto: "))
if(cate==1 and sueldo==5000000):
    c1=sueldo+(sueldo*0.10)
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruot es: ",c1)
elif(cate==2 and sueldo==4300000):
    c2=sueldo+(sueldo*0.15)
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruot es: ",c2)
elif(cate==3 and sueldo==3600000):
    c3=sueldo+(sueldo*0.20)
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruot es: ",c3)
elif(cate==4 and sueldo==2000000):
    c4=sueldo+(sueldo*0.40)
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruot es: ",c4)
elif(cate==5 and sueldo==900000):
    c5=sueldo+(sueldo*0.60)
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruto es: ",c5)
else:
    print ("su categoria es: ",cate)
    print("su nuevo sueldo bruto es: ",sueldo)