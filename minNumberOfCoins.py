def minNumberOfCoins(n, denoms):
    ways = [float("inf") for amount in range(n+1)]
    ways[0] = 0

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                if (denom-amount) < ways[amount]:
                    ways[amount] = ways[amount-denom]+1

    return ways[n]


a = minNumberOfCoins(18, [1, 2, 4, 5, 6])
