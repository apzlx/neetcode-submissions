class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target>nums[-1] or target < nums[0]:
            return -1

        l = 0
        r = len(nums)

        while l<=r:
            i = (r-l)//2 + l
            mid = nums[i]
            if mid == target:
                return i
            elif mid < target:
                l = i+1
            else:
                r = i-1

        return -1