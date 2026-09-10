class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if original or rotated n times, then nums[-1] > nums[0]
        # then min is just nums[0]

        # need to find the beginning of the original array, call it min, where all the ones to the left of it are > than it, and all the ones to the right are > than it
        # if we start at the middle and see 

        if nums[-1] >= nums[0]:
            return nums[0]

        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[r] > nums[l]:
                return nums[l]
            mid = (l+r)//2
            if mid == 0 or mid == len(nums)-1:
                return min(nums[mid], nums[l], nums[r])
            if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                return nums[mid]
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return 0
