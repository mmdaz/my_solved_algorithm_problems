def tribonacci_element (signature , n) :
    if n == 0 :
        return signature[0]
    if n == 1 :
        return signature[1]
    if n == 2 :
        return signature[2]
    else:
        return tribonacci_element(signature , n-1) + tribonacci_element(signature , n-2) + tribonacci_element(signature , n-3)


def tribonacci(signature, n):
    #your code here
    numbers = []
    if n == 0 :
        return numbers

    for i in range (n) :
        numbers.append(tribonacci_element(signature , i))

    return numbers

nums = [0.5,0.5,0.5]
print(tribonacci_element(nums , 5))
print(tribonacci(nums , 30))
