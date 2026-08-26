class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        neighbors = defaultdict(list)

        for a,b in prerequisites:
            neighbors[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for k,v in indegree.items():
            if v == 0:
                q.append(k)

        possible = 0
        res = []
        while q:
            node = q.popleft()
            possible += 1
            res.append(node)
            for n in neighbors[node]:
                indegree[n] -= 1
                if not indegree[n]:
                    q.append(n)
        
        return res if possible == numCourses else []
