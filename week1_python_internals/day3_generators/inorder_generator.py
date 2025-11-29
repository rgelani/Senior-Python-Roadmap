# ----------------------------------------------------------------------
# File: inorder_generator.py
# Concept: Python Generators for Memory-Efficient DSA Traversal
#
# This implementation uses 'yield' to process nodes one at a time,
# avoiding the O(N) space complexity required to store the full result list.
# ----------------------------------------------------------------------

class Node:
    """
    A basic Node structure for the Binary Search Tree (BST).
    Included here for the generator function to be self-contained and runnable.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal_generator(root):
    """
    Performs an In-order traversal of a binary tree using a generator.

    This function yields keys one by one (lazy evaluation), which means 
    it has O(h) space complexity (where h is the tree height, for the call stack) 
    instead of O(N) space complexity needed to store the full list result.

    It uses the 'yield from' expression, which is efficient syntactic sugar 
    for delegating to a subgenerator.

    Args:
        root: The root node of the binary tree.
    """
    if root is not None:
        # 1. Traverse Left Subtree Recursively using yield from
        # 'yield from' delegates control to the subgenerator
        yield from inorder_traversal_generator(root.left) 
        
        # 2. Yield the Root Key (The actual value processing)
        yield root.key 
        
        # 3. Traverse Right Subtree Recursively using yield from
        yield from inorder_traversal_generator(root.right)

# ----------------------------------------------------------------------
# Example Usage (For local testing of this file):
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Create a small test tree:
    #      10
    #     /  \
    #    5    15
    #   / \
    #  3   7
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    
    print("In-Order Traversal (Generator Output):")
    
    # We loop over the generator object to consume the values
    traversal_gen = inorder_traversal_generator(root)
    
    for key in traversal_gen:
        print(key, end=" ")
    
    # Expected output: 3 5 7 10 15 
    print("\n\nDemonstration of Laziness:")
    
    lazy_gen = inorder_traversal_generator(root)
    
    print("First value yielded:", next(lazy_gen)) 
    print("Second value yielded:", next(lazy_gen))
    print("Code executes only up to the point of the 'yield' call.")