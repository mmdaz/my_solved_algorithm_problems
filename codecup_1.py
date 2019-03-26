reghim = input()

r_counter = 0
g_counter = 0
y_counter = 0

for s in reghim:
    if s == 'G':
        g_counter += 1
    elif s == 'R':
        r_counter +=1
    else:
        y_counter += 1

if r_counter >= 3:
    print("nakhor lite")
elif y_counter >= 2 and r_counter >=2:
    print("nakhor lite")
elif g_counter == 0:
    print("nakhor lite")
else:
    print("rahat baash")
