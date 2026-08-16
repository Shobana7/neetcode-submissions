class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        neighbors = defaultdict(list)

        for x,y in prerequisites:
            indegree[x] += 1
            neighbors[y].append(x)
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        possibility = 0
        while q:
            node = q.popleft()
            possibility += 1
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return numCourses == possibility



        

        

