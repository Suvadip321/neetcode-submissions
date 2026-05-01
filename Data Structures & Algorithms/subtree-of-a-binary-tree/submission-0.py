# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def isSameTree(s, t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return (isSameTree(s.left, t.left) and isSameTree(s.right, t.right))
            return False
        if not t:
            return True
        if not s:
            return False
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)