class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))

        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minH:
            time, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return time
            
            for dr in direc:
                neiR, neiC = r + dr[0], c + dr[1]

                if (neiR, neiC) in visit:
                    continue

                if 0 <= neiR < N and 0 <= neiC < N and (neiR, neiC) not in visit:
                    visit.add((neiR, neiC))
                    heapq.heappush(minH, [max(time, grid[neiR][neiC]), neiR, neiC])


        