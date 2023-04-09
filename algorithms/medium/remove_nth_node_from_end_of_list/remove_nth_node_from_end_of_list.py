# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vals = []
        while True:
            vals.append(head.val)
            if head.next is None:
                break

            head = head.next

        vals = vals[::-1]
        del vals[n-1]
        
        node = None
        for v in vals:
            if node is None:
                node = ListNode(val=v, next=None)
            else:
                node = ListNode(val=v, next=node)

        return node
