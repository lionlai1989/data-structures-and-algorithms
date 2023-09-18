#!/usr/bin/env python3

import sys

class Node():

    def __init__(self, value, counter, is_terminal) -> None:
        self.value = value
        self.counter = counter
        self.is_terminal = is_terminal
        self.children = {}

    def __repr__(self,):
        return "grader cannot handle this"
        # return (
        #     f"Value: {self.value}, "
        #     f"Counter: {self.counter}, "
        #     f"Children: {self.children}, "
        #     f"is_terminal: {self.is_terminal}"
        # )

def dfs(node, trie):
    if not node.is_terminal:
        # node is not terminal so trie needs to allocate a new place for node.
        trie[node.counter] = {}

        for character in node.children:
            
            # Get counter from children.
            counter = dfs(node.children[character], trie)

            tmp = {character: counter}

            trie[node.counter].update(tmp)
        
        # After all children are processed, return its counter.
        return node.counter
    
    else:
        return node.counter

def build_trie(patterns):
    """
    Return the trie built from patterns
    in the form of a dictionary of dictionaries,
    e.g. {0:{'A':1,'T':2},1:{'C':3}}
    where the key of the external dictionary is
    the node ID (integer), and the internal dictionary
    contains all the trie edges outgoing from the corresponding
    node, and the keys are the letters on those edges, and the
    values are the node IDs to which these edges lead.
    """

    # print(f"patterns: {patterns}")

    global_counter = 0

    # Create root with empty string and assume it is not the end.
    root = Node("", global_counter, False)

    for pattern in patterns:
        # Each new pattern starts searching from root.
        node = root

        for character in pattern:


            if character in node.children:
                # character is already added.
                node = node.children[character]
            else:
                # character has not been added.
                global_counter += 1

                new_node = Node(character, global_counter, False)

                # Add new node to the children of the current node.
                node.children[character] = new_node

                node = new_node

        # After a pattern is finished being processed, the last node is terminal. 
        node.is_terminal = True
    
    # Create a trie to fulfill this task.
    trie = dict()
    dfs(root, trie)

    return trie


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
