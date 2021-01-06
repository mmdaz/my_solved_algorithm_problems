def countbits(n):
    counter = 0
    for c in '{0:b}'.format(n):
        if int(c) == 1:
            counter += 1
    return counter


print(countbits(10))