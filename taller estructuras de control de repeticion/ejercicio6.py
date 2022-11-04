datos=input()
(n,k)=datos.split(" ")
n=int(n)
k=int(k)
y=n%k
c=0
for i in range(n,y,-k):
    n=n+1
    if(n!=0):
        c=c+1
print(c)