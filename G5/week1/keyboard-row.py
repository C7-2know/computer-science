class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=["qwertyuiop","asdfghjkl","zxcvbnm"]
        out_pt=[]
        for i in range(len(words)):
            for k in range(len(keyboard)):
                for j in range(len(words[i])):
                    if words[i][j].lower() not in keyboard[k]:
                        break
                else:
                    out_pt.append(words[i])
                    break
        return out_pt