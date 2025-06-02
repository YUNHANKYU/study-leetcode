def maxProfit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    print(max_profit)

    return max_profit


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([7, 6, 4, 3, 1])
maxProfit([2, 4, 1])


def maxProfitDP(prices: list[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i-1], prices[i] - min_price)

    print(dp[-1])
    return dp[-1]


maxProfitDP([7, 1, 5, 3, 6, 4])
maxProfitDP([7, 6, 4, 3, 1])
maxProfitDP([2, 4, 1])
