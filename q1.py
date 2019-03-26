import math

q = int(input())

circls = []
for i in range(q):
    command = input()
    x = int(command.split(" ")[1])
    y = int(command.split(" ")[2])
    r = int(command.split(" ")[3])
    if command.split(" ")[0] == "A":
        flag1 = False
        for circle in circls:
            if math.sqrt((int(circle.split(" ")[0]) - x) * (int(circle.split(" ")[0]) - x) + (
                    int(circle.split(" ")[1]) - y) * (int(circle.split(" ")[1]) - y)) < int(circle.split(" ")[2]) + r:
                print("No")
                flag1 = True
                break
        if not flag1:
            print("Ok")
            circls.append("{} {} {}".format(x, y, r))
    else:
        flag = False
        for circle in circls:
            if x == int(circle.split(" ")[0]) and y == int(circle.split(" ")[1]) and r == int(circle.split(" ")[2]):
                circls.remove(circle)
                print("Ok")
                flag = True
                break
        if not flag:
            print("No")
