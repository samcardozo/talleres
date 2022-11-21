estudiantes = { "1": { "nombre": "Lorea", "nota": 8 }, 
"2": { "nombre": "Markel", "nota": "4.2" }, 
"3": { "nombre": "Julen", "nota": 6.5 } } 
N=0
canestu=int(input("cantidad estudiantes: "))
estu={}
aprovados=[]
suspendidos=[]
t=0
while True:
    N=N+1
    b=str(input("nombre: "))
    a=float(input("nota: "))
    dicc={N:{"nombre": b, "nota": a}}
    estu.update(dicc)
    t=t+a
    if(a>=6):
        aprovados.append(b)
    if(a<6):
        suspendidos.append(b)
        prom=(t/canestu)
    if(N==canestu):
        break
print("diccionario",estu)
print("aprovados",aprovados)
print("suspendidos: ",suspendidos)
print(f"promedio: {prom:.2f}")