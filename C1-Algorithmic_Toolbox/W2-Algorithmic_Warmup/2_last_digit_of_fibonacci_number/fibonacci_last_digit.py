# python3


def fibonacci_last_digit(n):
    # Naive solution:
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10


def fibonacci_last_digit_fast(n):
    # Faster solution: Avoid adding two large numbers because it's SLOW.
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        res = (previous + current) % 10
        previous = current
        current = res
    return current % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_last_digit_fast(n))
