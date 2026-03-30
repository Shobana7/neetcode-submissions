class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = defaultdict(int)
        neighbors = defaultdict(list)

        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            neighbors[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        res = []

        while q:
            node = q.popleft()
            count += 1
            res.append(node)
            for n in neighbors[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if count != numCourses:
            return []
        
        return res