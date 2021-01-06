year = input()
result = int(year) + 1

while(True):
    set1 = set(str(result))
    result = int(result)
    if (len(set1) != 4) :
        result +=1
        continue
    else:
        break
print(result)