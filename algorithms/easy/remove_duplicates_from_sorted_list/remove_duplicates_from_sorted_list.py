# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        targets = []
        while True:
            if head.val not in targets:
                targets.insert(0, head.val)
            if head.next == None:
                break
                
            head = head.next
        
        nodes = ListNode(val=targets[0], next=None)
        for idx, val in enumerate(targets):
            if idx == 0:
                continue
            nodes = ListNode(val=val, next=nodes)
        
        return nodes