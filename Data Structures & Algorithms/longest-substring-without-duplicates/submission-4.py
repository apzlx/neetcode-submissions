class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring without duplicate
        # brute force: two loops
        if len(s)<2:
            return len(s)

        l, r = 0, 0
        s_list = [c for c in s]
        unique = set()

        index_dict = defaultdict(int) # key - char, val - last seen index
        max_length = 0
        curr_length = 0

        while r < len(s):
            r_char = s_list[r]
            if r_char in unique:
                l = max(index_dict[r_char], l)
                curr_length = r - l
            else:
                unique.add(r_char)
                curr_length+=1
            index_dict[r_char] = r
            max_length = max(max_length, curr_length)
            r+=1

        return max_length

            



