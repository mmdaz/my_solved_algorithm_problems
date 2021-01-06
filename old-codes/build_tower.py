"""


"""

def floor_builder (num , max_num):
    floor = ""
    for i in range(1 , max_num + 1):
        if i in range (int((max_num + 1)/2) - int((num - 1 ) / 2) , int((max_num + 1)/2 + (num - 1 ) / 2 + 1 )):
            floor += "*"
        else:
            floor += " "
    return floor


def tower_builder(n_floors):
    n_floors = 2 * n_floors - 1
    result = []
    for i in range (1 , n_floors + 1 , 2):
        result.append(floor_builder(i,n_floors))

    return result



print(tower_builder(3))