n, k = input().split(" ")

n = int(n)
k = int(k)

l = []
r = []

for i in range(n):
    tl, tr = input().split(" ")
    l.append(tl)
    r.append(tr)

wait_times = sum(r)

