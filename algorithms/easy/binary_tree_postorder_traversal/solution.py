# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        orders = []
        self.postorder(root, orders)

        return orders
        
    def postorder(self, root: TreeNode, orders: list):
        if root.left is not None:
            self.postorder(root.left, orders)
        
        if root.right is not None:
            self.postorder(root.right, orders)

        orders.append(root.val)

solution = Solution()
print(solution.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None)))==[3,2,1])
print(solution.postorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None))), TreeNode(3, None, TreeNode(8, TreeNode(9, None, None), None))))==[4,6,7,5,2,9,8,3,1])
print(solution.postorderTraversal(None)==[])
print(solution.postorderTraversal(TreeNode(1, None, None))==[1])