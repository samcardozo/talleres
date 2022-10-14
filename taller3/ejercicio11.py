#ejercicio11
f=int(input("temperatura: "))
if(f>85):
    print("debera practicar natacion")
elif(f>70 and f<=85):
    print("debera practicar tenis")
elif(f>32 and f<=70):
    print("debera practicar golf")
elif(f>10 and f<=32):
    print("debera practicar esqui")
elif(f>(-4) and f<=10):
    print("debera practicar marcha")
else:
    print("no deberia practicar deporte")