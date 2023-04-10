# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head

        heads = []
        while True:
            if head.val != val:
                heads.append(head.val)

            head = head.next
            if not head:
                break

        head = None
        for v in heads[::-1]:
            head = ListNode(val=v, next=head)

        return head