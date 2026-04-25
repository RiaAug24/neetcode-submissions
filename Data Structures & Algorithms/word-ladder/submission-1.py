class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)
        visit = {word: 0 for word in wordList}

        if beginWord == endWord:
            return 1

        if endWord not in wordList: return 0

        res = float('inf')
        beginArr = [x for x in beginWord]
        visit[beginWord] = 1

        q = deque([[beginArr, 1]])

        while q:
            cur, seq = q.popleft()
 
            for i in range(m):
                temp = cur.copy()
                for k in range(ord('a'), ord('z')+1):
                    if k == temp[i]:
                        continue
                    temp[i] = chr(k)
                    tmp_str = "".join(temp)
                    if tmp_str == endWord:
                 
                        res = min(res, seq+1)
                    else:
                        if tmp_str in wordList and not visit[tmp_str]:
                            q.append([temp.copy(), seq+1])
                            visit[tmp_str] = 1
            
        return res if res != float('inf') else 0

            
        
