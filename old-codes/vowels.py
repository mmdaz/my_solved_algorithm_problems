def getCount(inputStr):
    num_vowels = 0
    # your code here
    for c in inputStr :
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' :
            num_vowels = num_vowels + 1

    return num_vowels


print(getCount("muha mmad"))