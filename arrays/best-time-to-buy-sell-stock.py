
from turtle import left


def maxProfit(prices):

    max_profit = 0
    leftpointer = 0  # buy
    rightpointer = 1  # sell

    while (rightpointer < len(prices)):

        today = prices[leftpointer]
        tomorrow = prices[rightpointer]
        curr_profit = tomorrow-today

        if (today < tomorrow):
            max_profit = max(max_profit, curr_profit)

        else:
            leftpointer = rightpointer
        rightpointer += 1

    return max_profit
