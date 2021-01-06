def maxProfit(prices):
    result_list = list()
    for index, p in enumerate(prices):
        for j in prices[index:]:
            if j - p > 0:
                result_list.append(j - p)
    if len(result_list) == 0:
        return 0
    else:
        return max(result_list)


print(maxProfit([7, 1, 5, 3, 6, 4]))
