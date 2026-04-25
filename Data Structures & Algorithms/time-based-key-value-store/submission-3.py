class TimeMap:

    def __init__(self):
        self.stamp = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stamp.keys():            
            self.stamp[key] = [[value, timestamp]]
        else:
            self.stamp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        stored_values = self.stamp.get(key, [])
        l = 0
        r = len(stored_values) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if stored_values[mid][1] <= timestamp:
                res = stored_values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


        
