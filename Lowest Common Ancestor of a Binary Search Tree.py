class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.getPath(root, p)
        q_path = self.getPath(root, q)

        lca = root
        for i in range(1, min(len(p_path), len(q_path))):
            if p_path[i].val == q_path[i].val:
                lca = p_path[i]
            else:
                break
        return lca


    def getPath(self, root, p):
        if p.val == root.val:
            return [ root ]

        node_stack = []
        node_stack.append((root, [ root ]))
        while len(node_stack) != 0:
            (node, path) = node_stack[-1]
            if node.val == p.val:
                return path
            node_stack = node_stack[:-1]
            if node.left != None:
                node_stack.append((node.left, path + [ node.left ]))
            if node.right != None:
                node_stack.append((node.right, path + [ node.right ]))