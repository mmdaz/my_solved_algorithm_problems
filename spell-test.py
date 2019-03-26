n = int(input())
mainstring = input()
teststring = input()

counter = 0

for m , t in zip(mainstring , teststring) :
    if m != t :
        counter += 1

print(counter)
