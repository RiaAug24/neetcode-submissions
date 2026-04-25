class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        new_triplets = []

        for x in triplets:
            if x[0] > target[0] or x[1] > target[1] or x[2] > target[2]:
                continue
            new_triplets.append(x)
        res = [0, 0, 0]
        
        for x in new_triplets:
            if x[0] == target[0]:
                res[0] = target[0]
        
            if x[1] == target[1]:
                res[1] = target[1]

            if x[2] == target[2]:
                res[2] = target[2]
            
        return True if res == target else False
            

        