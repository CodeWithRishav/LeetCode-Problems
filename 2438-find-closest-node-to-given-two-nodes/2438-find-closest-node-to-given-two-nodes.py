class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        def gen(src):
            dist = [inf] * n
            dist[src] = 0
            
            pq = [(0, src)]
            
            while pq:
                weight, node = heappop(pq)
                
                if edges[node] == -1 or weight != dist[node]: continue
                    
                nei = edges[node]
                
                old = dist[nei]
                new = weight + 1
                
                if new < old:
                    dist[nei] = new
                    heappush(pq, (new, nei))
            
            return dist
        dist1 = gen(node1)
        dist2 = gen(node2)
        
        res = inf
        index = 0
        for i, (a, b) in enumerate(zip(dist1, dist2)):
            s = max(a, b)
            if s < res:
                res = s
                index = i
        
        return -1 if res == inf else index
        