def likes (names) :
    if len(names) == 0 :
        print("no one likes this")
    if len(names) == 1 :
        print(names[0] + " likes this")
    if len(names) == 2 :
        print(names[0] + " and " + names[1] + " likes this")
    if len(names) == 3 :
        print(names[0] + ", " + names[1] + " and " + names[2] + " likes this")
    if len(names) > 3 :
        print(names[0] + ",  " + names[1] + " and "  + str(len(names)-2) + " others like this")


names = ['1', '2', '3', '4']

likes(names)

