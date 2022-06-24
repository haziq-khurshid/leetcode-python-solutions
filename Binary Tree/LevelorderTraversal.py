# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]                              # Add root to Queue
        
        while queue:                                
            curr_level = []                         # Initialize current level as empty for each level
            len_queue = len(queue)
            for i in range(len_queue):              # Run loop till size of queue
                node = queue.pop(0)
                if node.left:       
                    queue.append(node.left)         # Append left node in queue
                if node.right:
                    queue.append(node.right)        # Append right node in queue
                curr_level.append(node.val)         # Append current node value in current level list
            res.append(curr_level)                  # Add current level list to the result
        return res