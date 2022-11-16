dicc={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lis=[]
for key in dicc:
    c=dicc[key]
    lis.append(c)
print(lis)
for i in lis:
    a=lis.count(i)
    if(a!=1):
        lis.remove(i)
print(lis)
