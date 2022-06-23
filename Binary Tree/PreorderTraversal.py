# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Recursive solution"""
        res = [] 
        if root:
            res += [root.val]                               # Add root value to reuslt
            res += self.preorderTraversal(root.left)        # Call recersive function for left side of node
            res += self.preorderTraversal(root.right)       # Call recursive function for right side of node
        return res

        """Iteratively Solution using stack
        res = []
        stack = [root]                                      # Add root node to stack            
        while stack:
            node = stack.pop()                              # While stack is not empty, take top node of stack
            if node:
                res.append(node.val)                        # Add node value to result
                stack.append(node.right)                    # Add right node to stack
                stack.append(node.left)                     # Add left node to stack (it will be on top)
        return res
        """