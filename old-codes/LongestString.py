def longest_consec(strarr, k):
    max_lenth = 0
    result_index = 0
    result_string = ""

    if k > len(strarr) or k <=0 or len(strarr) == 0:
        return ""

    for i in range (len(strarr) - k + 1):
        temp = 0
        for j in range (k):
            temp +=  len(strarr[i+j])
        if temp > max_lenth:
            max_lenth = temp
            result_index = i

    for i in range (k):
        result_string += strarr[result_index + i]

    return result_string



print(longest_consec(["ali" , "muhammad" , "erfan"] , 2))