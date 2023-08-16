def fibonacci_sum(n):
    # Naive solution
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_faster(n):
    # Faster solution
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_faster(n))
