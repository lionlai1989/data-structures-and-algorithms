# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    idx = None

    for i, current in enumerate(text, start=1): # Use 1-based numbering. Demanded by the task.
        if current in "([{":
            # Process opening bracket.
            opening_brackets_stack.append(Bracket(current, i))

        if current in ")]}":
            # Process closing bracket.

            # Stack is empty. The current is problematic.
            if len(opening_brackets_stack) == 0:
                return True, i

            bracket = opening_brackets_stack.pop()
            character, idx = bracket.char, bracket.position
            # brackets do not match.
            if not are_matching(character, current):
                return True, i

    if len(opening_brackets_stack) != 0:
        bracket = opening_brackets_stack.pop()
        character, idx = bracket.char, bracket.position
        return True, idx
    else:
        return False, idx


def main():
    text = input()
    mismatch, idx = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == True:
        print(idx)
    elif mismatch == False:
        print("Success")
    else:
        print("Something is wrong.")

if __name__ == "__main__":
    # Use the following as input:
    # {}[]
    # 
    # (())
    main()
