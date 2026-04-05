# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        
        while current!=None:
            values.append(current.val)
            current = current.next
        
        values.reverse()

        dummy = ListNode()
        current = dummy

        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next