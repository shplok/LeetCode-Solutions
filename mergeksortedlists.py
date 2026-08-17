# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(l, r):
    dummy = ListNode(0)
    tail = dummy
    while l and r:
        if l.val < r.val:
            tail.next = l
            l = l.next
        else:
            tail.next = r
            r = r.next
        tail = tail.next
    tail.next = l if l else r
    return dummy.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
                return None
        elif len(lists) == 1:
            return lists[0]
        
        i = 0
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    merged_lists.append(merge(lists[i], lists[i+1]))
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists
        return lists[0]
