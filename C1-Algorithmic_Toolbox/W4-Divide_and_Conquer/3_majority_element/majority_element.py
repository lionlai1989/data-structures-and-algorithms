def majority_element_naive(elements):
    # Naive solution:
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element_faster(elements):
    # Faster solution:
    total_len = len(elements)
    
    # Create a table to store the times of occurences of the elements
    # table: {value: occurence}
    table = {}

    for element in elements:
        if element in table:
            table[element] += 1
        else:
            table[element] = 1
    
    for key in table.keys():
        if table[key] > total_len // 2:
            return 1
    return 0

if __name__ == '__main__':
    # Use the following as input:
    # 5
    # 2 3 9 2 2
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_faster(input_elements))
