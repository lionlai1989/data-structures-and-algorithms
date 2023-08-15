from sys import stdin

def sort_with_indices(lst):
    # Descending order
    sorted_indices = sorted(range(len(lst)), key=lambda i: lst[i], reverse=True)
    sorted_list = [lst[i] for i in sorted_indices]
    return sorted_list, sorted_indices

def optimal_value(capacity, weights, values):
    value = 0.

    value_per_weight = [v/w for v, w in zip(values, weights)]
    _, descending_indices = sort_with_indices(value_per_weight)

    for idx in descending_indices:
        if capacity == 0:
            return value
        a = min(capacity, weights[idx])
        value = value + a * values[idx] / weights[idx]
        capacity = capacity - a

    # print(capacity, weights, values)

    return value


if __name__ == "__main__":
    # Use the following as input:
    # 3 50
    # 60 20
    # 100 50
    # 120 30
    # <ctrl-d> sends EOF
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
