class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force: for each digit, find the longest consecutive sequence from that digit, this takes O(n^2)
        # only need to know the count, not the actual sequence
        # keep track of k where k is the last number in the longest consecutive sequence, and we look for k+1
        nums_set = set(nums)
        start_value = set()

        for n in nums:
            if (n-1) not in nums_set:
                start_value.add(n)
        print(start_value)
        
        longest = 0
        for n in start_value:
            j = n+1
            count = 1
            while j in nums_set:
                count+=1
                j+=1
            
            longest = max(longest, count)
        return longest