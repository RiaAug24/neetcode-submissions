class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.MAX = capacity
        self.idx = 0
        

    def get(self, key: int) -> int:
        print(self.cache)
        if key not in self.cache.keys():
            return -1
        else:
            self.cache[key][1] = self.idx
            self.idx += 1
            return self.cache[key][0]


    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key] = [value, self.idx]
        elif len(self.cache) == self.MAX:
            lru = [-1, 1001]
            for x in self.cache.keys():
                if self.cache[x][1] < lru[1]:
                    lru[0] = x
                    lru[1] = self.cache[x][1]
            self.cache.pop(lru[0])
            self.cache[key] = [value, self.idx]
        else:
            self.cache[key] = [value, self.idx]
        self.idx += 1

        
