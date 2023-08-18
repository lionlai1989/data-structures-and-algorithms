from sys import stdin

def maximum_gold(capacity, weights):
    num_items = len(weights)

    # value: (num_items, capacity+1)
    value = [[0 for x in range(capacity + 1)] for y in range(num_items)]

    for i in range(0, num_items):
        for capa in range(0, capacity + 1):
            value[i][capa] = value[i-1][capa]

            if weights[i] <= capa:
                val = value[i - 1][capa - weights[i]] + weights[i]
                if value[i-1][capa] < val:
                    value[i][capa] = val

    return value[num_items-1][capacity]


if __name__ == '__main__':
    # Use the following as input:
    # 10 3
    # 1 4 8
    # <ctrl-d>
    # 
    # 20 10
    # 5 4 5 10 9 6 6 6 8 8
    # <ctrl-d>
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
