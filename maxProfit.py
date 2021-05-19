def findMaxProfit(price, k):
    n = len(price)

    profit = [[None for x in range(n)] for y in range(k + 1)]

    for i in range(k + 1):
        for j in range(n):
            if i == 0 or j == 0:
                profit[i][j] = 0
            else:
                max_so_far = 0
                for x in range(j):
                    curr_price = price[j] - price[x] + profit[i - 1][x]
                    if max_so_far < curr_price:
                        max_so_far = curr_price

                profit[i][j] = max(profit[i][j - 1], max_so_far)

    return profit[k][n - 1]

