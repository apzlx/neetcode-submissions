class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k replacement to get longest substring that has only one character
        # brute force: get all distinct characters and see for each character if we can fill in the gaps between left most and right most under k

        l = 0
        # l, r tracks the current length of the substring

        most_freq = 0
        most_freq_char = ""
        freq_dict = {}

        for r in range(len(s)):
            if s[r] not in freq_dict:
                freq_dict[s[r]] = 1
            else:
                freq_dict[s[r]] += 1

            if freq_dict[s[r]] > most_freq:
                most_freq_char = s[r]

            most_freq = freq_dict[most_freq_char]

            if (r-l+1) - most_freq > k:
                freq_dict[s[l]] -= 1
                l+=1
        
        return len(s)-l
            