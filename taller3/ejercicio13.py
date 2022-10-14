#ejercicio13
dia=int(input("dia de nacimiento: "))
mes=int(input("mes de nacimiento: "))
año=int(input("año de nacimiento: "))
if(mes==11):
    if(dia>=1 and dia<=22):
        print("su signo es escorpion")
    else:
        print ("su signo es sagitario")
elif(mes==12):
    if(dia>=1 and dia<=21):
        print("su signo es sagitario")
    else:
        print ("su signo es capricornio")
elif(mes==1):
    if(dia>=1 and dia<=20):
        print("su signo es capricornio")
    else:
        print ("su signo es acuario")
elif(mes==2):
    if(dia>=1 and dia<=19):
        print("su signo es acuario")
    else:
        print ("su signo es piscis")
elif(mes==3):
    if(dia>=1 and dia<=19):
        print("su signo es piscis")
    else:
        print ("su signo es aries")
elif(mes==4):
    if(dia>=1 and dia<=20):
        print("su signo es aries")
    else:
        print ("su signo es tauro")
elif(mes==5):
    if(dia>=1 and dia<=21):
        print("su signo es tauro")
    else:
        print ("su signo es geminis")
elif(mes==6):
    if(dia>=1 and dia<=21):
        print("su signo es geminis")
    else:
        print ("su signo es cancer")
elif(mes==7):
    if(dia>=1 and dia<=22):
        print("su signo es cancer")
    else:
        print ("su signo es leo")
elif(mes==8):
    if(dia>=1 and dia<=23):
        print("su signo es leo")
    else:
        print ("su signo es virgo")
elif(mes==9):
    if(dia>=1 and dia<=22):
        print("su signo es virgo")
    else:
        print ("su signo es libra")
elif(mes==10):
    if(dia>=1 and dia<=22):
        print("su signo es libra")
    else:
        print ("su signo es scorpion")
edad=2022-año
print("tu edad para el año 2022 sera de: ",edad)