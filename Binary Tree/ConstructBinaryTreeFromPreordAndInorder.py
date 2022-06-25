# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:                             # Return when either list is empty
            return None
        root = TreeNode(preorder.pop(0))                            # Take left most node of Preorder as root, it will always be root
        mid = inorder.index(root.val)                               # Find index of root in Inorder list
        root.left = self.buildTree(preorder, inorder[:mid])         # Left side of root node in Inorder will be left subtree
        root.right = self.buildTree(preorder, inorder[mid+1:])      # Right side of root node in Postorder will be right subtree
        return root