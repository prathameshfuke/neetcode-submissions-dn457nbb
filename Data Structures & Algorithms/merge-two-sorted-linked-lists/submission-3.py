class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []

        current = l1
        while current!=None:
            values.append(current.val)
            current = current.next

        current = l2
        while current!=None:
            values.append(current.val)
            current = current.next

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for v in values:
            current.next = ListNode(v)
            current= current.next
        
        return dummy.next
            


