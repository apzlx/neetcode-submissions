class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res[i] = index of the 1st num that is > temperatures[i]
        # brute force: go from left to right, for each index, go find the next index that is greater than temperatures[i]
        # worst case: O(n2) for desc array

        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            curr_temp = temperatures[i]
            if not stack:
                res[i] = 0
                stack.append([curr_temp, i])
            else:
                while stack:
                    if curr_temp >= stack[-1][0]:
                        stack.pop()
                        continue
                    else:
                        res[i] = stack[-1][1] - i
                        break
                    
                stack.append([curr_temp, i])

        return res


            