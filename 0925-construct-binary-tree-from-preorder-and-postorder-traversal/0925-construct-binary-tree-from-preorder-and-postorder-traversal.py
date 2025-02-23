# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:idx], post[:idx-1])
        root.right = self.constructFromPrePost(pre[idx:], post[idx-1:-1])
        return root