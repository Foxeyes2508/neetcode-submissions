class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                l+=1
            else:
                r-=1
        return -1