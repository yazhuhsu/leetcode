# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None and l2 == None:
            return None
        
        if l1 == None and l2 != None:
            return l2
        
        if l1 != None and l2 == None:
            return l1
        
        result = ListNode()
        l3 = ListNode()
        
        if l1.val <= l2.val:
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
            
        result = l3
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
            
        while l1 != None:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        
        while l2 != None:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next
            
        return result
        
        