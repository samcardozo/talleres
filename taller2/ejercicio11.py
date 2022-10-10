#ejer11
nombre=input("ingrese nombre: ")
horanorm=int(input("numero de horas normales trabajadas: "))
pagohnor=int(input("pago por hora normal trabajada: "))
horaextra=int(input("numero de horas extras trabajadas: "))
pagohextr=pagohnor+(pagohnor*0.25)
print("pago por hora extra: ", pagohextr)
sueldobase=(horanorm*pagohnor)+(horaextra*pagohextr)
print("sueldo base: ",sueldobase)
print("deducciones")
parfor=sueldobase*0.05
print("paro forzoso: ", parfor )
polihabi=sueldobase*0.02
print("politica habitacional: ", polihabi)
cajahorro=sueldobase*0.07
print("caja ahorro: ", cajahorro)
dedu=parfor+polihabi+cajahorro
print("total en deducciones: ", dedu)
print("asignaciones")
print("actualizacion academica: 250000 COP")
hijos=int(input("ingrese cantidad de hijos: "))
xniño=hijos*173000
print("por hijo: ", xniño)
print("prima por hogar: 180000 COP")
totalasig=250000+xniño+180000
print("total en asignaciones: ", totalasig )
suelnet=(sueldobase-dedu)+totalasig
print("sueldo neto: ",suelnet)