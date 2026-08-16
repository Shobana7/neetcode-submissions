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
        
        possibility = []
        while q:
            node = q.popleft()
            possibility.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return numCourses == len(possibility)



        

        

