def filter_list(l):
    'return a new list with the strings filtered out'
    new_list = []
    for c in l:
        if str(c).isdigit() :
            new_list.append(c)
    return new_list


l = [1 , 2 , 'a']
print(filter_list(l))