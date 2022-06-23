# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recusrive Solution"""
        res = []
        if root:
            res += self.postorderTraversal(root.left)               # Call recursive function where root is left node
            res += self.postorderTraversal(root.right)              # Call recursive funciton where root is right node
            res += [root.val]                                       # Add root to result
        return res

        """ Iterative Solution
        res = []
        stack = [root]                                              # Add root node to stack
        while stack:
            node = stack.pop()                                      # Take top node of stack
            if node:
                res.append(node.val)                                # Add top node value to result
                stack.append(node.left)                             # Add left node to stack
                stack.append(node.right)                            # Add right node to stack
        
        return res[::-1]                                            # Return result in reverse order as we appended it in reverse order
        """