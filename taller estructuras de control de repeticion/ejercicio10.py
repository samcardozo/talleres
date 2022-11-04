#Dado  la  altura  de    n    estudiantes  de  la  universidad,  hallar  la mayor de todas las alturas.
c=0
est=int(input("cantidad estudiantes: "))
edades1=[]
while True:
    if(c==est):
        break
    edad=int(input("edad: "))
    edades1.append(edad)
    c=c+1
edades1.sort()
p=edades1[0]
print(p)