# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:                            # Return when either list is empty
            return None
        root = TreeNode(postorder.pop())                            # Create root node from right most value of postorder(as this is always root)
        mid = inorder.index(root.val)                               # Find index of root node in inorder queue
        root.right = self.buildTree(inorder[mid+1:], postorder)     # Left side of root node in Inorder will be left subtree
        root.left = self.buildTree(inorder[:mid], postorder)        # Right side of root node in Inorder will be right subtree
        return root