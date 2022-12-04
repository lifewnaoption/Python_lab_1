class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 and t2:
            # Merge the values from two trees
            node = TreeNode(t1.val + t2.val)
            
            # Merge the left trees using the function recursively
            node.left = self.mergeTrees(t1.left, t2.left)
            
            # Merge the right trees using the function recursively
            node.right = self.mergeTrees(t1.right, t2.right)
            
            return node
            
        else:
            return t1 or t2