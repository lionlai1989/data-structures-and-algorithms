def gcd(a, b):
    # Naive solution:
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd

def gcd_faster(a, b):
    # Faster solution:
    if b == 0:
        return a
    else:
        return gcd_faster(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_faster(a, b))
