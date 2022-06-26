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
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            dummy = Node(0)                     # Dummy node before start at each level
            curr = dummy                        # Point curr pointer to dummy node
            while node:
                if node.left:                   # If node conains left child, move current pointer to it
                    curr.next = node.left
                    curr = curr.next
                if node.right:                  # If node contains right child, move current pointer to it
                    curr.next = node.right
                    curr = curr.next
                node = node.next                # Move node to its next
            node = dummy.next                   # When node is null i.e. end of level. Move node to the next level
                                                # Next of dummy is start of next level
        return root
        