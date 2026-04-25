class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize != 0: return False

        hand.sort()

        inGroup = [False] * n
        prev = []

        for i in range(n):
            # print(inGroup)
            if inGroup[i]:
                continue
            group = []
            if not prev:
                j = i    
            else:
                j = prev[0]
                prev.remove(j)
            while j < n and len(group) != groupSize:
                if inGroup[j]:
                    j += 1
                    continue
                elif group and group[-1] == hand[j]:
                    prev.append(j)
                else:
                    group.append(hand[j])
                    if j in prev:
                        prev.remove(j)
                    inGroup[j] = True
                j += 1
            
            if len(group) != groupSize:
                return False

            for i in range(len(group)-1):
                if group[i] + 1 != group[i+1]:
                    return False

        return True
        
        