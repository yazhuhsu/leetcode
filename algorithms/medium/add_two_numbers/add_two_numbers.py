# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        
        carry = 1
        while l1 or l2:
            if l1:
                num1 = num1 + l1.val*carry
                l1 = l1.next
            if l2:
                num2 = num2 + l2.val*carry
                l2 = l2.next
            
            carry *= 10
            
        num_sum = num1+num2
        nums = list(map(int, str(num_sum)))
        
        node = None
        for num in nums:
            node = ListNode(num, node)
            
        return node
            