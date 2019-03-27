import math
def solution(s1: str, s2: str):
    current_index = 0
    time = 0
    for c in s2:
        c_index = s1.index(c)
        time += int(math.fabs(c_index-current_index))
        current_index = c_index
    print(time)

solution("abcdefghijklmnopqrstuvwxyz", "cba")