"""

NOT COMPLETED .!

"""


def unique_in_order(iterable):

    iterable = list(iterable)
    lenth = len(iterable)

    for i in range(0 , len(iterable)):
        if i <=  (lenth - 1 ):
            print(i)
            if iterable[i] == iterable[i + 1]:
                del iterable[i+1]

    return iterable


print(unique_in_order(['A', 'B', 'C', 'D', 'A', 'A', 'B', 'B', 'B']))