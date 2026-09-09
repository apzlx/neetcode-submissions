class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # go from left to right, if curr bar height is smaller than the top of the stack, pop that bar, and calculate the area by bar height * (curr_index - stack[-1][1]+1)
        stack = [] # store [height, index]
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] <= stack[-1][0]:
                prev_low = stack.pop()
                height = prev_low[0]
                if stack:
                    width = i - stack[-1][1] - 1
                else:
                    width = prev_low[1] + 1

                max_area = max(height * width, max_area)

            stack.append([heights[i], i])

        while stack:
            top = stack.pop()
            if stack:
                max_area = max(top[0]*(len(heights)-stack[-1][1]-1), max_area)
            else:
                max_area = max(top[0]*len(heights), max_area)

        return max_area
