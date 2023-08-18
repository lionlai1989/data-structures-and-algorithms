# NOTE: numpy is not allowed in the grading system.
# import numpy as np

def edit_distance(first_string, second_string):
    """The edit distance between two strings is defined as the minimum
    number of single-symbol insertions, deletions, and substitutions to
    transform one string into the other one.
    """

    # An (m+1, n+1) matrix:
    #
    #     0 d i s t a n c e
    #   0 0 1 2 3 4 5 6 7 8
    #   e 1 - - - - - - - -
    #   d 2 - - - - - - - -
    #   i 3 - - - - - - - -
    #   t 4 - - - - - - - -
    #   i 5 - - - - - - - -
    #   n 6 - - - - - - - -
    #   g 7 - - - - - - - -

    m = len(first_string)
    n = len(second_string)

    # arr: (m+1, n+1) array. 
    arr = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Initialize first column
    for i in range(m + 1):
        arr[i][0] = i
    # Initialize first row
    for j in range(n + 1):
        arr[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = arr[i][j - 1] + 1
            deletion = arr[i - 1][j] + 1
            match = arr[i - 1][j - 1]
            mismatch = arr[i - 1][j - 1] + 1

            if first_string[i - 1] == second_string[j - 1]:
                arr[i][j] = min(insertion, deletion, match)
            else:
                arr[i][j] = min(insertion, deletion, mismatch)

    return arr[m][n]


if __name__ == "__main__":
    # Use the following as input:
    # editing
    # distance
    # 
    # short
    # ports
    print(edit_distance(input(), input()))
