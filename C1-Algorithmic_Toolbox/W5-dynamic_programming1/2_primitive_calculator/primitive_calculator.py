def compute_operations(n):
    """Find the minimum number of operations needed
    to get a positive integer n from 1 by using only
    three operations: add 1, multiply by 2, and mul-
    tiply by 3.
    Input: An integer n.
    Output: The minimum number
    of operations “+1”, “x2”, and “x3”
    needed to get n from 1.
    """

    min_operations = [0 for _ in range(n+1)] # Minimum operations for the interger n.
    true_operations = [None for _ in range(n+1)]

    for value in range(2, n+1): # Skip 0 and 1 because they should be 0.
        min_operations[value] = float('inf')

        # There are three possible routes. `backtrack` must be set to either of three. 
        backtrack = None

        if value % 3 == 0:
            # 1st route: x3
            num_operation = min_operations[value // 3] + 1 # value // 3 must be an integer.
            if num_operation < min_operations[value]:
                min_operations[value] = num_operation
                backtrack = "x3"

        if value % 2 == 0:
            # 2nd route: x2
            num_operation = min_operations[value // 2] + 1 # value // 2 must be an integer.
            if num_operation < min_operations[value]:
                min_operations[value] = num_operation
                backtrack = "x2"

        # 3rd route: +1
        num_operation = min_operations[value - 1] + 1
        if num_operation < min_operations[value]:
            min_operations[value] = num_operation
            backtrack = "+1"
        
        assert backtrack != None
        true_operations[value] = backtrack

    # Backtracking the whole series back to 1.
    sequence = []
    value = n # Start from the input integer.
    backtrack = true_operations[value] # start from the last operation.
    sequence.append(value)

    while value != 1:
        # backtrack must be either one of be three operations. 
        if backtrack == "+1":
            value = value - 1

        elif backtrack == "x3":
            assert value % 3 == 0
            value = value // 3

        elif backtrack == "x2":
            assert value % 2 == 0
            value = value // 2

        else:
            raise ValueError("Something is horribly wrong.")

        backtrack = true_operations[value]
        sequence.append(value)

    sequence.reverse()
    # NOTE: Explain why I cannot return `sequence.reverse()` directly
    # I.e., `return sequence.reverse()` does not work.
    return sequence


if __name__ == '__main__':
    # Use the following as input:
    # 96234
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
