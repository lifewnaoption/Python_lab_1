class Solution(object):
    def isValidBST(self, root):
        pre, stack = None, []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if pre and pre.val >= node.val:
                return False
            pre = node
            root = node.right