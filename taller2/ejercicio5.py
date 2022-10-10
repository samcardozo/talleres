#ejer5
par1=int(input("ingrese calificacion parcial 1: "))
par2=int(input("ingrese calificacion parcial 2: "))
par3=int(input("ingrese calificacion parcial 3: "))
exfin=int(input("ingrese calificacion examen final: "))
trabfin=int(input("ingrese calificacion trabajo final: "))
totpar= ((par1+par2+par3)/3)*0.55
totexam= exfin*0.30
tottf= trabfin*0.15
totmater=totpar+totexam+tottf
print("caificacion final: ", totmater)