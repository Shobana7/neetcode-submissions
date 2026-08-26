class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i: 0 for i in range(numCourses)}
        neighbors = defaultdict(list)

        for a,b in prerequisites:
            indegree[a] += 1
            neighbors[b].append(a)
        
        q = deque()
        for k,v in indegree.items():
            if v == 0:
                q.append(k)

        possible = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                possible += 1
                for n in neighbors[node]:
                    indegree[n] -= 1
                    if not indegree[n]:
                        q.append(n)
        
        return possible == numCourses

