class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        neighbors = defaultdict(list)

        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        q = deque()
        q.append((0,-1))

        visit = set()
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nx in neighbors[node]:
                if nx == parent:
                    continue
                if nx in visit:
                    return False
                q.append((nx, node))
                visit.add(nx)
        
        return len(visit) == n
