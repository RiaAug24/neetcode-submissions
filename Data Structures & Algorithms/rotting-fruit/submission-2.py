class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        

        visit = set()
        q = deque()

        def addToQueue(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return
            
            q.append([r, c])
            visit.add((r, c))

        count_1 = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                if grid[r][c] == 1:
                    count_1 += 1

        if count_1 == 0:
            return 0

        minutes = -1
        print(q)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2
                addToQueue(r-1, c)
                addToQueue(r+1, c)
                addToQueue(r, c-1)
                addToQueue(r, c+1)
            
            minutes += 1

        print(grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes

        

        