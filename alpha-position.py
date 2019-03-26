import string
def alphabet_position(text):
    pos_list = []
    for c in text :
        if c.isalpha() :
            pos_list.append(str(ord(c.lower())-96))
    return " ".join(pos_list)



text = "I love you nioosha"
print(alphabet_position(text))