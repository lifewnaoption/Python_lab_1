class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        curA, curB = headA, headB
        while curA != curB:
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next
            
        return curA