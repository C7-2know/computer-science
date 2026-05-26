class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        ans =[]
        for l in word:
            if l.islower() and l.upper() in word:
                ans.append(l)
        return len(ans)