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

        current = head
        i=0

        while current!=None:
            current.val = values[i]
            i = i+1
            current = current.next

        return head


        