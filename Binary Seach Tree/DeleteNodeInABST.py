# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.val:                                         # If current root is the one to be deleted
            if not root.left:                                       # If left child does't exist, return right child
                return root.right
            if not root.right:                                      # If right child doesn't exist return left child
                return root.left
            minNode = self.successor(root.right)                    # If both child exists, Find successor for current node
            root.right = self.deleteNode(root.right, minNode.val)   # Delete the successor node from right subtree
            minNode.left = root.left                                # Attach left subtree to left of successor
            minNode.right = root.right                              # Attach right subtree to right of successor
            root = minNode                                          # Return successor node as root
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
    
    # Successor helper function to find next successor from right subtree
    def successor(self, node):
        while node.left:
            node = node.left
        return node
