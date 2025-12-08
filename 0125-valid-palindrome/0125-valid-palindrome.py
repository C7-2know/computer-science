class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s = s.upper()
        print(left, right)
        while left< right:           
            while left<right and not s[left].isalpha():
                if s[left].isnumeric():
                    break
                left +=1
            while left< right and not s[right].isalpha():
                if s[right].isnumeric():
                    break
                right -=1
           
            if s[left]!= s[right]:
                return False
            left+=1
            right-=1
        return True