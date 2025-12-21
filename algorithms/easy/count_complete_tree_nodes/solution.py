# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        counter = self.count(root)

        return counter

    def count(self, root: TreeNode) -> int:
        counter = 0
        if self.isComplete(root):
            counter += 1

        if root.left is not None:
            counter += self.count(root.left)

        if root.right is not None:
            counter += self.count(root.right)

        return counter

    def isComplete(self, root: TreeNode) -> bool:
        if root.left is not None and root.right is not None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is None:
            return True

        return False

solution = Solution()
print(solution.countNodes(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, TreeNode(6, None, None), None)))==6)
print(solution.countNodes(TreeNode(1, None, None))==1)
print(solution.countNodes(None)==0)