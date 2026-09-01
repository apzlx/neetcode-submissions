class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s)-1
        
        while front<back:
            if not(s[front].isalpha() or s[front].isdigit()):
                front+=1
                continue
            if not(s[back].isalpha() or s[back].isdigit()):
                back-=1
                continue
            if s[front].lower() == s[back].lower():
                front+=1
                back-=1
                continue
            return False
        
        return True