usuarios = {"iperurena": {"nombre": "Iñaki", "apellido": "Perurena","password": "123123"}, 
"fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
"aolaizola": { "nombre": "Aimar", "apellido": "Olaizola", "password": "123456" }} 
N=0
while True:
    usu=str(input("usuario: "))
    con=int(input("contraseña: "))
    a=usu in usuarios
    b=con in usuarios.values()
    c=usuarios["nombre"]
    d=usuarios["apellido"]
    if(a==True):
        print(c)
        print(d)
        break
    N=N+1
    if(N==3):
        break

