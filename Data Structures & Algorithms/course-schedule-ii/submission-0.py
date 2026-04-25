class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)

        res = []
        visit = set()

        def dfs(c):
            if c in visit:
                return False

            if preMap[c] == []:
                if c not in res:
                    res.append(c)
                return True
            
            visit.add(c)
            
            for p in preMap[c]:
                if not dfs(p):  return False
            
            visit.remove(c)
            preMap[c] = []
            if c not in res:
                res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
            if c not in res:
                res.append(c)

        return res