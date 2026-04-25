import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = collections.Counter(tasks)
        maxHeap = [-x for x in task_freq.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        cycle = 0
        while queue or maxHeap:
            cycle += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, cycle + n])
            if queue and cycle == queue[0][1]:
                cnt, cycle = queue.popleft()
                heapq.heappush(maxHeap, cnt)
            
        return cycle     
        
        
        
        
        
        
        
        
        
        

            

        