# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        tail = curr 
        next_node = None
        i = left
        
        
        while i <= right and curr:
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
            i += 1
        
        prev.next = next_node
        tail.next = curr
        
        return dummy.next
