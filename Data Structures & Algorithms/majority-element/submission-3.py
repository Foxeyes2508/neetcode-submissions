class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candi=0
        count=0
        for num in nums:
            if count==0:
                candi=num
            if num==candi:
                count+=1
            else:
                count-=1
        return candi