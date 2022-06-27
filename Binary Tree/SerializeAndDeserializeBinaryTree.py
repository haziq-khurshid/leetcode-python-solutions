# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return 'null'                      # If node is null, return 'null' as string
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
                        # Return string by joining current root value with left subtree and right subtree using recursion
    
    def deserialize(self, data):
        def deserialize_helper(queue):                  # Helper function for recursive calls
            if queue[0] == 'null':                      # If first element is 'null', remove it & return Null
                queue.pop(0)
                return None
            root = TreeNode(queue[0])                   # Create a node using first element from queue and remove from queue
            queue.pop(0)
            root.left = deserialize_helper(queue)       # Take left node of root using remaining queue
            root.right = deserialize_helper(queue)      # Take right node of root using remaining queue
            return root                                 # Return root
        
        queue = data.split(',')                        # Convert input string to a Queue
        return deserialize_helper(queue)               # Call helper function with Queue as input