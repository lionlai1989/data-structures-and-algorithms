def binary_search(keys, query):

    # print(keys, query)

    # zero-based indexing array.
    left, right = 0, len(keys) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if keys[mid] == query:
            # mid is the 0-th element. so it must be first occurence.
            if mid - 1 == -1:
                return mid

            # if keys[mid-1] is also query, it means keys[mid] is not
            # the first occurence. Check the middle point on the left.
            if keys[mid - 1] != query:
                return mid
        
        if query > keys[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    # Use the following as input:
    # 7
    # 2 4 4 4 7 7 9
    # 4
    # 9 4 5 2
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
