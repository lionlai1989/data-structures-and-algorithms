def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, minimum_table, maximum_table, operators):
    minimum = float('inf')
    maximum = float('-inf')

    for k in range(i, j):
        a = evaluate(maximum_table[i][k], maximum_table[k+1][j], operators[k])
        b = evaluate(maximum_table[i][k], minimum_table[k+1][j], operators[k])
        c = evaluate(minimum_table[i][k], maximum_table[k+1][j], operators[k])
        d = evaluate(minimum_table[i][k], minimum_table[k+1][j], operators[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum

def maximum_value(dataset):
    # Use one-based indexing. It's easier to learn with the algorithm presented
    # in the course.
    operators = [op for op in dataset[1::2]]
    operators.insert(0, 0)
    numbers = [int(x) for x in dataset[0::2]]
    numbers.insert(0, 0)
    len_numbers = len(numbers)

    # Let E[i][j] be the subexpression d[i] operator[i] ... operator[j-1] d[j]
    # Define:
    # minimum_table[i][j] as minimum value of E[i][j]
    # maximum_table[i][j] as maximum value of E[i][j]
    minimum_table = [[0 for x in range(len_numbers)] for y in range(len_numbers)]
    maximum_table = [[0 for x in range(len_numbers)] for y in range(len_numbers)]
    
    # Initialize elements in main diagonal.  
    for i in range(1, len_numbers):
        minimum_table[i][i], maximum_table[i][i] = numbers[i], numbers[i]

    for s in range(1, len_numbers - 1):
        for i in range(1, len_numbers - s):
            j = i + s
            minimum_table[i][j], maximum_table[i][j] = MinAndMax(i, j, minimum_table, maximum_table, operators)

    return maximum_table[1][-1]


if __name__ == "__main__":
    # Use the following as input:
    # 5-8+7*4-8+9
    # 
    # 1-2*3
    print(maximum_value(input()))
