# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    opening_brackets_stack = []

    # Use 1-based numbering. Demanded by the task.
    for i, current in enumerate(text, start=1):
        # Process opening bracket.
        if current in "([{":
            opening_brackets_stack.append(Bracket(current, i))

        # Process closing bracket.
        if current in ")]}":
            # Stack is empty. The current is problematic.
            if len(opening_brackets_stack) == 0:
                return i

            bracket = opening_brackets_stack.pop()
            character, idx = bracket.char, bracket.position

            # brackets do not match.
            if not are_matching(character, current):
                return i

    # If there are remaining brackets in the stack,
    if len(opening_brackets_stack) != 0:
        bracket = opening_brackets_stack.pop()
        character, idx = bracket.char, bracket.position
        return idx
    else:
        return -1


def main(text):
    mismatch = find_mismatch(text)

    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    # text = "[]"
    # main(text)
    # text = "{}[]"
    # main(text)
    # text = "[()]"
    # main(text)
    # text = "(())"
    # main(text)
    # text = "{[]}()"
    # main(text)
    # text = "{"
    # main(text)
    # text = "{[}"
    # main(text)
    # text = "foo(bar);"
    # main(text)
    
    text = input()
    main(text)