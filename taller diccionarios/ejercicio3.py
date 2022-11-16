usuarios = {"iperurena": {"nombre": "Iñaki", "apellido": "Perurena","password": "123123"}, 
"fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
"aolaizola": { "nombre": "Aimar", "apellido": "Olaizola", "password": "123456" }} 
N=0
while True:
    N=N+1
    usu=str(input("usuario: "))
    con=str(input("contraseña: "))
    if(N==3):
        break
    else:
        for x,y in usuarios.items():
            if(usu in x and con in y["password"]):
                print(y["nombre"])
                print(y["apellido"])
                break


