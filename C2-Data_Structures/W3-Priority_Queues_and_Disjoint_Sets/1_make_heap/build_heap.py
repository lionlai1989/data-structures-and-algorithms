# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def left_child(i):
    return 2 * i

def right_child(i):
    return 2 * i + 1

                        
def build_heap_faster(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    NOTE: The solution here uses 1-based indexing which is the same
    as the lecture's so the implementation is easiwer.
    But, it needs to return 0-based indexing as
    required by the assignment.
    """
    # data: 5 4 3 2 1
    size = len(data)
    # Prepend 0 to data so it's 1-based array.
    data.insert(0, 0)
    swaps = []


    def sift_down(i):
        min_index = i
        left = left_child(i)
        if left <= size and data[left] < data[min_index]:
            min_index = left
        right = right_child(i)
        if right <= size and data[right] < data[min_index]:
            min_index = right
        if i != min_index:
            # swap `data[i]` and `data[min_index]`.
            data[i], data[min_index] = data[min_index], data[i]
            
            swaps.append((i, min_index))
            
            sift_down(min_index)

    # Calculate starting index. As long as it's non-negative,
    # it's safe to use int() to get floor of a floating-point
    # number.
    start = int(size / 2)
    for i in range(start, 0, -1): # start, start-1, ..., 1
        sift_down(i)

    return swaps


def main():
    # Use the following as input:
    # 5
    # 5 4 3 2 1
    # 
    # Output:
    # 3
    # 1 4
    # 0 1
    # 1 3
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap_faster(data)

    print(len(swaps))
    for i, j in swaps:
        # Convert 1-based to 0-based indexing as required by
        # the assignment.
        print(i - 1, j - 1)


if __name__ == "__main__":
    main()
