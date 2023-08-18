def binary_search(keys, query):

    # print(keys, query)

    # zero-based indexing array.
    left, right = 0, len(keys) - 1

    while left <= right:
        # NOTE: (left + right) // 2
        # The famous integer-overflow bug undetected for 20 years if using C++.
        mid = left + (right - left) // 2
        if keys[mid] == query:
            return mid

        if query > keys[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    # Use the following as input:
    # 5
    # 1 5 8 12 13
    # 5
    # 8 1 23 1 11
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
