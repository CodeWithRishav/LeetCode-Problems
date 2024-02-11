class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[[-1] * n for _ in range(n)] for _ in range(m)]
        f[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
        for i in range(1, m):
            for j1 in range(n):
                for j2 in range(n):
                    x = grid[i][j1] + (0 if j1 == j2 else grid[i][j2])
                    for y1 in range(j1 - 1, j1 + 2):
                        for y2 in range(j2 - 1, j2 + 2):
                            if 0 <= y1 < n and 0 <= y2 < n and f[i - 1][y1][y2] != -1:
                                f[i][j1][j2] = max(f[i][j1][j2], f[i - 1][y1][y2] + x)
        return max(f[-1][j1][j2] for j1, j2 in product(range(n), range(n)))