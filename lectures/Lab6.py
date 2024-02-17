t=[]
for i in range(9):
    l=[]
    for j in range(9):
        l.append((i+1)*(j+1))
    t.append(l)
print(t)
print(t[1][0])