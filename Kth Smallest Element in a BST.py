def inorder(root,res,k):
    if root==None:return
    heapq.heappush(res,-root.val)
    if len(res)>k:heapq.heappop(res)
    inorder(root.left,res,k)
    inorder(root.right,res,k)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        heapq.heapify(res)
        inorder(root,res,k)
        return -res[0]