class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p != q:
            return False
        self.isSameTree(self.isSameTree(p.left,q.left),self.isSameTree(p.right,q.right))
        return True

a = Solution()
a.isSameTree()