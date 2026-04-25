class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [[x, y] for x, y in zip(position, speed)]
        sorted_car = sorted(car, reverse = True)
        print(sorted_car)
        stack = []
        for x in (sorted_car):
            time = (target - x[0]) / x[1]
            if len(stack) == 0:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        print(stack)

        return len(stack)

            
        

            
        

        