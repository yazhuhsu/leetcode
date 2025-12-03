# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        p_orders, q_orders = [], []
        self.traversal(p, p_orders)
        self.traversal(q, q_orders)

        if p_orders == q_orders:
            return True

        return False

    def traversal(self, node: TreeNode, orders: list):
        orders.append(node.val)

        if node.left is not None:
            self.traversal(node.left, orders)
        else:
            orders.append(None)

        if node.right is not None:
            self.traversal(node.right, orders)
        else:
            orders.append(None)

solution = Solution()

p = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
q = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
print(solution.isSameTree(p, q)==True)

p = TreeNode(1, TreeNode(2, None, None), None)
q = TreeNode(1, None, TreeNode(2, None, None))
print(solution.isSameTree(p, q)==False)

p = TreeNode(2, TreeNode(2, None, TreeNode(2, TreeNode(2, None, None), None)), TreeNode(2, None, None))
q = TreeNode(2, TreeNode(2, TreeNode(2, None, None), None), TreeNode(2, TreeNode(2, None, None), None))
print(solution.isSameTree(p, q)==False)
