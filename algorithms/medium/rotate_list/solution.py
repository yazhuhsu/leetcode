# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        origin = []
        while head.next is not None:
            origin.append(head.val)
            head = head.next
        
        origin.append(head.val)

        if k > len(origin):
            k = k % len(origin)

        new = origin[len(origin)-k:]+origin[:len(origin)-k]

        head.val = new[len(new)-1]
        for idx in range(len(new)-2, -1, -1):
            head = ListNode(val=new[idx], next=head)

        return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def listVals(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

solution = Solution()
# Rotate right by 2: [1,2,3,4,5] → [4,5,1,2,3]
print(listVals(solution.rotateRight(buildList([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3])
# k > len: 4%3=1, [0,1,2] → [2,0,1]
print(listVals(solution.rotateRight(buildList([0, 1, 2]), 4)) == [2, 0, 1])
# k=0: no rotation
print(listVals(solution.rotateRight(buildList([1, 2]), 0)) == [1, 2])
# single node
print(listVals(solution.rotateRight(buildList([1]), 5)) == [1])
# None head
print(solution.rotateRight(None, 3) is None)