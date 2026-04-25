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

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    
                addToQueue(r-1, c)
                addToQueue(r+1, c)
                addToQueue(r, c-1)
                addToQueue(r, c+1)
            minutes += 1

        if fresh: return -1
        return minutes

        

        