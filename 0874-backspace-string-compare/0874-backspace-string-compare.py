class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        for i in s:
            if i=="#" and st:
                st.pop()
            elif i!='#':
                st.append(i)
        tt=[]
        for i in t:
            if i=="#" and tt:
                tt.pop()
            elif i!="#":
                tt.append(i)
        return "".join(st)=="".join(tt)