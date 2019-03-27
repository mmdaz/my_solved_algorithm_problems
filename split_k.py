def solution(inp: str, k):
    splitted_inp = inp.split("-")
    inp = inp.replace("-", "")
    lengh = len(inp)
    inp = inp.upper()
    rem = lengh % k
    print(lengh)
    # print(rem)
    if rem == 0:
        for i in range(lengh, lengh, k):
            print("ds")
            inp = inp[:i] + "-" + inp[i:]

    print(inp)

solution("ads-fasf-aas", 2)