class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        #Put number in small first
        heapq.heappush(self.small,-num)

        #make sure small's biggest < large's smallest
        if self.small and self.large and -self.small[0]>self.large[0]:
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        #balance sizes
        if len(self.small)>len(self.large):
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large)>len(self.small):
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-val)
    def findMedian(self)->float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        return (-self.small[0]+self.large[0])/2

    #def findMedian(self) -> float:
        
        