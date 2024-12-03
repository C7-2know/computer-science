class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out=""
        prev=0
        for i in spaces:
            out+=s[prev:i]
            out+=" "
            prev=i
        
        return out+s[prev:]