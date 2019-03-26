

def check(name1 , name2 , p , q):
    b1 = True
    b2 = True

    for i in range(p):
        if name1[i] != name2[i]:
            b1 = False
            break
        else:
            b1 = True

    for i in range(q):
        if name1[len(name1)- i -1] != name2[len(name2)- i -1]:
            b2 = False
            break
        else:
            b2 = True

    if b1 and b2:
        return True
    else:
        return False


n ,p , q =  map(int , input().split())
names = []
for i in range(n):
    names.append(input())

names.sort()

for i in names:
    for j in names[names.index(i) + 1:]:

        if i[0] != j[0] :
            break
        if check(i,j,p,q):
            names.remove(j)


print(len(names))