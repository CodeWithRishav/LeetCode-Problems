class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # <=3 also working, same as <=1
                # i==j, or i+1==j
                dp[i][j] = s[i] == s[j] and (abs(i - j) <= 1 or dp[i + 1][j - 1])

        def dfs(s, i, t):
            nonlocal n # note: still pass OJ without this nonlocal. default is non-local
            if i == n:
                ans.append(t.copy())
                return
            for j in range(i, n): # including single char dp[i][i]
                if dp[i][j]:
                    t.append(s[i : j + 1])
                    dfs(s, j + 1, t)
                    t.pop(-1)

        dfs(s, 0, [])
        return ans
        