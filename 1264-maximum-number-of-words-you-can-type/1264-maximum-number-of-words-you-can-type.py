class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken={l for l in brokenLetters}
        words=text.split()
        count = 0
        for word in words:
            for l in word:
                if l in broken:
                    break
            else:
                count += 1
        return count
