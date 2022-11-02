class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cov = ListNode(next=head)
        curr  = cov
        
        while head:
            if head.val == val:
                curr.next, head = head.next, head.next
            else:
                curr, head = curr.next, head.next
        
        return cov.next