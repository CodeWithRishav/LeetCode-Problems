class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        graph = collections.defaultdict(list)
        
        for x, y in relations:
            graph[y].append(x)
                
        @cache
        def go(x):
            res = 0
            
            for child in graph[x]:
                res = max(res, go(child))
            
            return res + time[x]
        
        return max(go(i) for i in range(1, n + 1))