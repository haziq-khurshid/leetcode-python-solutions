"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []                                  # Stack to track nodes in order as we do Depth First Traversal
        curr = head                                 # Current pointer at head
        prev = None                                 # Previous pointer at null
        while curr:
            curr.prev = prev                        
            if curr.next:                           # If next exists, add it to stack
                stack.append(curr.next)
            if curr.child:                          # If child exists, add it to stack
                stack.append(curr.child)
            curr.child = None                       # Setting current child to none because we are flatenning the list
            prev = curr                             # Bring previous pointer to current
            if stack:                               # Move current pointer to top node in stack
                curr.next = stack.pop()
            curr = curr.next
        return head