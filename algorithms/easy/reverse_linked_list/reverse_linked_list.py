# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        heads = []
        while head != None:
            heads.append(head.val)
            head = head.next

        head = None
        for h in heads:
            head = ListNode(val=h, next=head)

        return head