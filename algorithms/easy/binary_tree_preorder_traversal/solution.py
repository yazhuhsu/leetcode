# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> []:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        orders = []
        self.preorder(root, orders)

        return orders

    def preorder(self, root: TreeNode, orders: []):
        orders.append(root.val)
        
        if root.left is not None:
            self.preorder(root.left, orders)
        
        if root.right is not None:
            self.preorder(root.right, orders)

solution = Solution()
print(solution.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None)))==[1,2,3])
print(solution.preorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None))), TreeNode(3, None, TreeNode(8, TreeNode(9, None, None), None))))==[1,2,4,5,6,7,3,8,9])
print(solution.preorderTraversal(None)==[])
print(solution.preorderTraversal(TreeNode(1, None, None))==[1])