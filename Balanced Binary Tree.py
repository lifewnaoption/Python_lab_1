def helper(root):
    if root is None:
        return 0
    d1 = helper(root.left)
    d2 = helper(root.right)
    if d1 == -1 or d2 == -1 or abs(d1-d2)>1:
        return -1
    else:
        return 1+max(d1,d2)
    
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = helper(root)
        if result==-1:
            return False
        else:
            return True