class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colors={}
        for i in range(k):
            colors[blocks[i]]=colors.get(blocks[i],0)+1
        opr=colors.get('W',0)
        for j in range(k,len(blocks)):
            colors[blocks[j-k]]-=1
            colors[blocks[j]]=colors.get(blocks[j],0)+1
            opr=min(colors.get('W',0),opr)
        return opr
            