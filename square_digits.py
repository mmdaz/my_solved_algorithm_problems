def square_digits (num) :
    digits = [d for d in str(num)]

    i = 0
    for d in digits :
        digits[i] = str(int(d)**2)
        i += 1

    digits = "".join(digits)
    digits = int(digits)
    return digits



n = 1234
print(square_digits(n))