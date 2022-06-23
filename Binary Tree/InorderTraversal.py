# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive Solution"""
        res = []
        if root:
            res += self.inorderTraversal(root.left)             # Call this function recursively by passing left of root as root node
            res += [root.val]                                   # Add root value to answer
            res += self.inorderTraversal(root.right)            # Call this function recursively by passing right of root as root node
        return res

        """ Iterative approach using Stack
        res = []
        stack = [root]                                          # Add root node to stack
        while stack:
            node = stack.pop()                                  # While stack is not empty,take top node
            if node:                                            
                stack.append(node.right)                        # Append right node to stack
                stack.append(node)                              # Append node to stack
                stack.append(node.left)                         # Append left node to stack (it will be on top)
            else:                                               
                if stack:                                       
                node = stack.pop()                              # If node is null and stack is not empty, take top node
                res.append(node.val)                            # Add value of top node to result
        return res
        """        
            
        