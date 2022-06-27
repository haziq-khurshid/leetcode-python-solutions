# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:                  # If root exists and contains either node , return root
            return root
        left = self.lowestCommonAncestor(root.left,p,q)             # Traverse left subtree
        right = self.lowestCommonAncestor(root.right,p,q)           # Traverse right subtree
        if left and right: return root                              # If nodes are in both left and right, return current root
        if left: return left                                        # If node is only on left subtree, return left
        else: return right                                          # If node is only on right subtree, return right