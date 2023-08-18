def change(money):
    # money: An integer money
    # Return: The minimum number of coins with denominations 1, 3, and 4 that changes money.
    denominations = [1, 3, 4]
    minimum_coins_for_money = [0 for i in range(money+1)]

    for m in range(1, money+1):
        minimum_coins_for_money[m] = float('inf')
        for coin in denominations:
            if m >= coin:
                num_coin = minimum_coins_for_money[m - coin] + 1
                if num_coin < minimum_coins_for_money[m]:
                    minimum_coins_for_money[m] = num_coin

    return minimum_coins_for_money[money] # the last element


if __name__ == '__main__':
    # Use the following as input:
    # 34
    m = int(input())
    print(change(m))
