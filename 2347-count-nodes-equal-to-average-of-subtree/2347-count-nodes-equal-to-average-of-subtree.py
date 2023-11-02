class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            ls, ln = dfs(root.left)
            rs, rn = dfs(root.right)
            s = ls + rs + root.val
            n = ln + rn + 1
            if s // n == root.val:
                nonlocal ans
                ans += 1
            return s, n

        ans = 0
        dfs(root)
        return ans