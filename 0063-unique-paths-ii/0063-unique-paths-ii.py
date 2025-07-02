class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]

        # dp[1][1] = dp[0][1] + dp[1][0]
        # so, set either dp[0][1]=1, or set dp[1][0]=1
        dp[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # else, ==1, obstacle, skip and leave as 0

        return dp[m][n]