# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == val: return root                 # If target value found, return current node
        if root.val > val:                              # If value is less than current node's value,
            return self.searchBST(root.left, val)       # Search Left Subtree
        else:
            return self.searchBST(root.right, val)      # Else, Search Right Subtree