# python3


def fibonacci_huge_naive(n, m):
    # Naive solution:
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def get_pisano_period(m):
    a = 0
    b = 1
    c = a + b
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1


def fibonacci_huge_fast(n, m):
    # Faster solution:
    pisano_period = get_pisano_period(m)
    remainder = n % pisano_period
    # print("pisano_period: ", pisano_period)
    # print("remainder: ", remainder)

    if remainder <= 1:
        return remainder

    prev = 0
    curr = 1
    temp = 0

    for _ in range(2, remainder + 1):
        temp = curr
        curr = (prev + curr) % m
        prev = temp
    return curr % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge_fast(n, m))
