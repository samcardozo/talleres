p=0
c=0
for i in range(1,1000):
    k=(i**2+1)/i
    p=p+k
    if(p<=1000):
        c=c+1
print(c)