h, str = input().split(" ")

h = int(h)
x = 0
for i in range(h+1):
    x += 2**i

steps = 0
leftest = x
rightest = x
L_reduction = 0
R_reduction = 0
step_amount = x


for s in str:
    if s == "L":
        leftest = x + 1 - (2**steps)
        L_reduction = (2 ** steps) + (leftest - step_amount)
        step_amount -= L_reduction
        steps += 1
    else:
        rightest = -1 * (2 ** (steps+1)) + 2 + x
        R_reduction = (2 ** (steps + 1)) - (step_amount - rightest)
        step_amount -= R_reduction
        steps += 1

print(step_amount)