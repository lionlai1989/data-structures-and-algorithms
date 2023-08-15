def fibonacci_number(n):
    # Naive solution:
    if n <= 1:
        return n
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number_faster(n):
    # Faster solution:
    if n <= 1:
        return n
    else:
        curr = 0 
        prev1 = 1
        prev2 = 0
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_faster(input_n))
