c=0
suma=0
ip=0
sp=0
est=int(input("cantidad estudiantes: "))
nombre=[]
puntajes=[]
while True:
    if(c==est):
        break
    name=str(input("nombre: "))
    puntaje=int(input("puntaje: "))
    nombre.append(name)
    puntajes.append(puntaje)
    c=c+1
max=puntajes[0]
for i in puntajes:
    if(i>max):
        max=i
min=puntajes[0]
for i in puntajes:
    if(i<min):
        min=i
for i in puntajes:
    suma=i+suma
pmayor=puntajes.index(max)
pmenor=puntajes.index(min)
nmayor=nombre[pmayor]
nmenor=nombre[pmenor]
prom=suma/est
for i in puntajes:
    if(i<prom):
        ip=ip+1
    if(i>prom):
        sp=sp+1
print("estudiante con mayor puntaje: ",nmayor)
print("estudiante con menor puntaje: ",nmenor)
print("mayor puntaje: ",max)
print("menor puntaje: ",min)
print("promedio puntajes: ",prom)
print("puntajes inferiores al promedio: ",ip)
print("puntajes superiores al promedio: ",sp)