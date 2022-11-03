datos=input()
(n,k)=datos.split(" ")
n=int(n)
k=int(k)
for i in range(n+1,k,-1):
    print(i-1)