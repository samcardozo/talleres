estudiantes = { "1": { "nombre": "Lorea", "nota": 8 }, 
"2": { "nombre": "Markel", "nota": "4.2" }, 
"3": { "nombre": "Julen", "nota": 6.5 } } 
N=0
canestu=int(input("cantidad estudiantes: "))
while True:
    estudiante1={}
    estudiantes={}
    N=N+1
    b=str(input("nombre: "))
    a=int(input("nota: "))
    estudiante1.update({b:a})
    estudiantes[N]=estudiante1
    if(N==canestu):
        break
print(estudiantes)