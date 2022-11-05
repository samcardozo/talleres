
consal=0
muj=0
hom=0
promedad=0
porcent=0
finales=1
y=0
b5=0
while True:
    a=str(input("¿consume licor? Y/N "))
    b=int(input("licor preferido: "))
    p=int(input("edad: "))
    s=str(input("sexo M/F: "))
    cont=str(input("¿desea continuar la investigacion? Y/N: "))  
    if(b==3):
        y=p+y
    if(b==5):
        b5=b5+1
    if(cont=="Y"):
        finales=finales+1
    if(a=="Y"):
        consal=consal+1
    if(s!="M" and p<=18):
        muj=muj+1
    if(s!="F" and p>=20 and p<=25):
        if(a=="N" or b!=1):
            hom=hom+1
    if(cont=="N"):
        break  
if(b==3):
    promedad=y/finales
porcent=(b5*100)/finales
print("Total de personas encuestadas que consumen licor: ",consal)
print("Total de mujeres menores de edad: ",muj)
print("Total, de hombres entre 20 y 25 años que no consumen aguardiente: ",hom)
print("Promedio de edad de las personas que consumen cerveza: ",promedad)
print("porcentaje de personas encuestadas que consumen whisky: ",porcent)