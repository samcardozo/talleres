#ejer6
clase=int(input("ingrese total de personas en la clase: "))
mujer=int(input("ingrese total de mujeres en la clase: "))
homb=int(input("ingrese total de hombres en la clase: "))
porhom=(homb*100)/clase
pormuj=(mujer*100)/clase
print("porcentaje de mujeres: ", pormuj)
print("porcentaje de hombres: ", porhom)