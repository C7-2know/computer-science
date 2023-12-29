class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(' ')
        words.sort(key=lambda i:i[-1])
        return " ".join(item[:-1] for item in words)