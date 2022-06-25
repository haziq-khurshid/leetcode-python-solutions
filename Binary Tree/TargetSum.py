# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and targetSum == root.val:          # If it is leaf node and targetSum matches node value, return True
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
                    # Call recursive function on left & right nodes while subtracting current node value from targetSum
                    # Thus, if remaining targetSum matches leaf node value, answer would be True                                                       