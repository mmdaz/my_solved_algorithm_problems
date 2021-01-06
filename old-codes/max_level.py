def find_shortest_path_from_two_index(i, j):
    vi = list()
    vj = list()
    while i != 0:
        vi.append(i % 2)
        i = int(i / 2)
    while j != 0:
        vj.append(j % 2)
        j = int(j / 2)
    vi_len = len(vi)
    vj_len = len(vj)
    k = 0
    if vi_len < vj_len:
        while k < vi_len and vi[k] == vj[k]:
            k += 1
    else:
        while k < vj_len and vi[k] == vj[k]:
            k += 1
    return vi_len + vj_len - 2 * k - 2


def solution(array: list):
    current_level_numbers = list()
    level_numbers_sum = list()
    current_dist = 0
    for index, num in enumerate(array):
        next_dist = find_shortest_path_from_two_index(0, index)
        if current_dist == next_dist:
            current_level_numbers.append(num)
            current_dist = next_dist
        else:
            level_numbers_sum.append(sum(current_level_numbers))
            current_dist = next_dist
    return level_numbers_sum.index(max(level_numbers_sum)) - 1
