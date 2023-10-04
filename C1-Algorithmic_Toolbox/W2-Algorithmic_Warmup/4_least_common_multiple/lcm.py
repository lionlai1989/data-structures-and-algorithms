# python3


def lcm(a, b):
    # Naive solution:
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l
    assert False


def gcd(a, b):
    # Faster solution for Greatest Common Divisor
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm_fast(a, b):
    # Faster solution: a * b = lcm(a, b) * gcd(a, b)
    return int(a * b / gcd(a, b))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_fast(a, b))
