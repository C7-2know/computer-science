class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=[set([i for i in "qwertyuiop"])]
        rows.append(set([i for i in "asdfghjkl"]))
        rows.append(set([i for i in "zxcvbnm"]))
        ans=[]
        for w in words:
            temp=w
            w=w.lower()
            row=0
            if w[0] in rows[1]:
                row=1
            elif w[0] in rows[2]:
                row=2
            for l in w:
                if l not in rows[row]:
                    break
            else:
                ans.append(temp)
        return ans
