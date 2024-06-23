class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i * 2 >= len(prices):
                return prices[i - 1]
            return prices[i - 1] + min(dfs(j) for j in range(i + 1, i * 2 + 2))

        return dfs(1)