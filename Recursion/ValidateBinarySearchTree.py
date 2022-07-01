# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def Valid(node,lower,upper):
            if not node: return True                        # Return true at leaf nodes
            if node.val <= lower or node.val >= upper:      # If condition for BST is violated, return False
                return False
            return Valid(node.left, lower, node.val) and Valid(node.right, node.val, upper)
                                                            # Else call recurively on left & right nodes
                                                            # by changing lower & upper bounds
        return Valid(root, float("-inf"),float("inf"))      # Calling helper function with negative and positive infinity as lower, upper bound