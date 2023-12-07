class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        word='f'*len(indices)
        for i in range(len(indices)):
            print
            if indices[i]+1==len(indices):
                word=word[:indices[i]]+s[i]
            else:
                word=word[:indices[i]]+s[i]+word[indices[i]+1:]   
        return word