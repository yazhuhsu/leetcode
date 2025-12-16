# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False

        left, right = [], []
        self.preorder(root.left, left)
        self.levelorder(root.right, right)

        for i in range(len(left)):
            if left[i] != right[i]:
                return False

        return True

    def preorder(self, root: TreeNode, orders: []):
        if root.left is None and root.right is None:
            orders.append(root.val)

        orders.append(root.val)

        if root.left is not None:
            self.preorder(root.left, orders)
        else:
            orders.append(-101)

        if root.right is not None:
            self.preorder(root.right, orders)
        else:
            orders.append(-101)
    
    def levelorder(self, root: TreeNode, orders: []):
        if root.left is None and root.right is None:
            orders.append(root.val)

        orders.append(root.val)

        if root.right is not None:
            self.levelorder(root.right, orders)
        else:
            orders.append(-101)

        if root.left is not None:
            self.levelorder(root.left, orders)
        else:
            orders.append(-101)

solution = Solution()
print(solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None))))==True)
print(solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None))))==False)
print(solution.isSymmetric(TreeNode(2, TreeNode(3, TreeNode(4, None, None), TreeNode(5, TreeNode(8, None, None), TreeNode(9, None, None))), TreeNode(3, TreeNode(5, TreeNode(9, None, None), TreeNode(8, None, None)), TreeNode(4, None, None))))==True)
print(solution.isSymmetric(TreeNode(5, TreeNode(2, TreeNode(4, None, TreeNode(1, TreeNode(2, None, None), None)), None), TreeNode(2, None, TreeNode(1, None, TreeNode(4, TreeNode(2, None, None), None)))))==False)
