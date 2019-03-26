def revers (word) :
    s = list(word)
    s = s[::-1]
    word = "".join(s)
    return word

def spin_words(sentence):
    # Your code goes here
    s = sentence.split(" ")

    i = 0
    for w in s :
        if len(w) > 4 :
            w = revers(w)
        s[i] = w
        i = i + 1

    sentence = " ".join(s)
    return sentence


sentence = "I love you nioosha"
print(spin_words(sentence))