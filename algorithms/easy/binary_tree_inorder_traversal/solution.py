# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if root == None:
            return []
        
        orders = []
        self.traversal(root, orders)

        return orders

    def traversal(self, node: TreeNode, orders: list):
        if node.left is not None:
            self.traversal(node.left, orders)

        orders.append(node.val)

        if node.right is not None:
            self.traversal(node.right, orders)

solution = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(solution.inorderTraversal(root)==[1,3,2])