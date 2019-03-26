
def duplicate_count (text) :
    counter = 0
    for c in text :
        if c in text[text.find(c) + 1 :] :
            counter = counter + 1
    return counter


text = "maryam"
print(duplicate_count(text))
