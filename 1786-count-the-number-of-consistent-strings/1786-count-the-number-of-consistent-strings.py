class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed=set([i for i in allowed])
        for st in words:
            set_=set([i for i in st])
            for l in set_:
                if l not in allowed:
                    break
            else:
                count+=1
        return count
        