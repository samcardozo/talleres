#ejer12
print("matematica")
matexam=int(input("ingrese calificacion examen: "))
matar1=int(input("ingrese calificacion tarea 1: "))
matar2=int(input("ingrese calificacion tarea 2: "))
matar3=int(input("ingrese calificacion tarea 3: "))
matxexam=matexam*0.90
matpromcalif=((matar1+matar2+matar3)/3)*0.10
totamat=matxexam+matpromcalif
print("calificacion: ", totamat)
print("fisica")
fisexam=int(input("ingrese calificacion examen: "))
fistar1=int(input("ingrese calificacion tarea 1: "))
fistar2=int(input("ingrese calificacion tarea 2: "))
fisxexam=fisexam*0.80
fispromcalif=((fistar1+fistar2)/2)*0.20
totafisi=fisxexam+fispromcalif
print("calificacion: ", totafisi)
print("quimica")
quimiexam=int(input("ingrese calificacion examen: "))
quimitar1=int(input("ingrese calificacion tarea 1: "))
quimitar2=int(input("ingrese calificacion tarea 2: "))
quimitar3=int(input("ingrese calificacion tarea 3: "))
quixexam=quimiexam*0.85
quipromcalif=((quimitar1+quimitar2+quimitar3)/3)*0.15
totaquimi=quixexam+quipromcalif
print("calificacion: ", totaquimi)
promtotal=(totamat+totafisi+totaquimi)/3
print("promedio de las tres calificaciones: ", promtotal)