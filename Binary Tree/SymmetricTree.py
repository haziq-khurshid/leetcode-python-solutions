# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursive Method"""
        def isMirror(left : TreeNode, right : TreeNode) -> bool:
            if not left and not right: return True              # If both nodes are null, return True
            if not left or not right: return False              # If either node is null, return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
                                                                # Return True if both values match,
                                                                # AND Left of left node matches right of right node
                                                                # AND Right of left node matches left of right node
        
        return isMirror(root.left, root.right)
        
        
        """Iterative Method

        if not root: return None
        queue = [root.left,root.right]                          # Add left and right nodes in queue
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right: continue                      # If both nodes are Null, skip current iteration of loop
            elif left and right and left.val == right.val: pass      # If values of both node matches, skip next else condition
            else: return False                                       # Else return False as Tree is not symmetric
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
        """    