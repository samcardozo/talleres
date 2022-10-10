#ejer9
hras=int(input("cantidad de horas trabajadas: "))
pres=int(input("pago por hora: "))
pagohora=hras*pres
impue=pagohora*0.20
sueldotot=pagohora-impue
print("sueldo neto: ", sueldotot)