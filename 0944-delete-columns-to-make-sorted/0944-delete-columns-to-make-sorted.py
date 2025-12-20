class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = [[word[i] for word in strs] for i in range(len(strs[0]))]
        count = 0
        for col in columns:
            if col!= sorted(col):
                count+=1
        return count