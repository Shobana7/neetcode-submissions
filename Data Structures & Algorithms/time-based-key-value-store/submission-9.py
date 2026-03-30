class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key]

        l,r = 0, len(values)-1

        while l < r:
            mid = l + (r-l)//2
            if values[mid][0] >= timestamp:
                r = mid
            else:
                l = mid + 1
        
        if values[l][0] > timestamp:
            l -= 1
        
        return "" if l < 0 else values[l][1]


            
        
