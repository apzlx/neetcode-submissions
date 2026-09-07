class Solution:
    def isValid(self, s: str) -> bool:
        # stack: filo
        p_dict = {"{":"}", "(":")", "[":"]"}

        stack = []
        for char in s:
            if char in p_dict:
                stack.append(char)
            else:
                if stack and p_dict[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        
        
                
            