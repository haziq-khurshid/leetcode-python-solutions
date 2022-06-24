# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0               # Base case: return 0 when node is null
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                                            # Call recursive method on left and righ tree separately
                                            # Take maximum between left & right side
                                            # Add 1 to count current level as well