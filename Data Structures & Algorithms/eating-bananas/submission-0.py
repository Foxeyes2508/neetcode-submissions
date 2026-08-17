import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
       # hrs=0
        while l<=r:
            n=(l+r)//2
            hrs=0
            for i in range(len(piles)):
                hrs+=math.ceil(piles[i]/n)
            if hrs<=h:
                r=n-1
            else:
                l=n+1
        return l