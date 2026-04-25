class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for i in range(len(gas)):
            gas_tank = gas[i]
            j = i
            seen = set()
            while True:
                if gas_tank < cost[j] or len(seen) == len(cost):
                    break
                
                gas_tank -= cost[j]
                seen.add(j)
                j = (j + 1) % len(cost)
                gas_tank += gas[j]

            if gas_tank > 0 and len(seen) == len(gas):
                return i
                
        return -1


            






        