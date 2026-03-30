class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        neighbors = defaultdict(set)
        indegree = defaultdict(int)

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            neighbors[b].add(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for n in neighbors[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if count == numCourses:
            return True
        
        return False

