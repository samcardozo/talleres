from msilib.schema import Media


a=str(input("¿consume licor? Y/N "))
b=int(input("licor preferido: "))
p=int(input("edad: "))
s=str(input("sexo M/F: "))
consal=0
mujmeno=0
homnoconsum=0
promedad=0
porcent=0
while True:
    if(a=="Y"):
        consal=consal+1
    if(s=="F" and p<=18):
        mujmeno=mujmeno+1
    if(s=="M" and b!=1 and p>=20 and p<=25 or s=="M" and a=="N" and p>=20 and p<=25):
        homnoconsum=homnoconsum+1
    cont=str(input("¿desea continuar la investigacion? Y/N: "))
    if(cont=="N"):
        break
    if(b==3):
        promedad=Media(s)
print("Total de personas encuestadas que consumen licor: ",consal)
print("Total de mujeres menores de edad: ",mujmeno)
print("Total, de hombres entre 20 y 25 años que no consumen aguardiente: ",homnoconsum)
print("Promedio de edad de las personas que consumen cerveza: ",promedad)