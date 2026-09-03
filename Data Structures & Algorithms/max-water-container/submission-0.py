class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # calculate the area from all bars left to right
        # O(n^2) 

        # opportunity to optimize:
        # area = min(heights[l], heights[r]) * (r-l)
        # if the r-l 

        l = 0
        r = len(heights)-1
        maxArea = 0
        while l<r:
            maxArea = max(min(heights[l], heights[r]) * (r-l), maxArea)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1

        return maxArea


        