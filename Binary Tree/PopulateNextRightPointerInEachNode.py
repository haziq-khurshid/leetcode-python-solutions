"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root and root.left and root.right:               # If node exists and is not a leaf node
            root.left.next = root.right                     # Point next of left node to right node
            if root.next:                                   # If next exists, it means we are in left subtree
                root.right.next = root.next.left            # Point next of right to left of next node
            self.connect(root.left)
            self.connect(root.right)
        return root