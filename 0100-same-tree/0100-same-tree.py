# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p or not q:
      return p == q # covers: p=none and q!=none, q=none and p!=none, both none
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)