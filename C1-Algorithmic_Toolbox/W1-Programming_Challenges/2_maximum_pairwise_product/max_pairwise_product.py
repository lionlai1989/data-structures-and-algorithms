# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0

    # naive solution
    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #             numbers[first] * numbers[second])

    # faster solution
    max_index1 = -1
    for first in range(n):
        if max_index1 == -1 or numbers[first] > numbers[max_index1]:
            max_index1 = first
    max_index2 = -1
    for second in range(n):
        if second != max_index1 and (
            (max_index2 == -1) or numbers[second] > numbers[max_index2]
        ):
            max_index2 = second
    max_product = numbers[max_index1] * numbers[max_index2]
    return max_product


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
