# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None                                # Return None if value not found
        if root.val == val: return root                         # If value equals to root value, return root
        if root.val > val:                                      # If value less than root value, solutions lies in left subtree
            return self.searchBST(root.left, val)               # Pass left of root as new root
        else:                                                   # Else solution lies in right subtree
            return self.searchBST(root.right, val)              # Pass right of root as new root
