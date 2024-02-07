class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        upd=[0 for _ in range(len(s))]
        for i in range(len(shifts)):
            st=shifts[i][0]
            end=shifts[i][1]
            ch=1
            if shifts[i][2]==0:
                ch=-1
            upd[st]+=ch
            if end+1<len(upd):
                upd[end+1]-=ch
        for k in range(1,len(upd)):
            upd[k]+=upd[k-1]
        s_arr=[]
        for z in range(len(s)):
            s_arr.append(ord(s[z])-97)
        s=''
       
        for p in range(len(s_arr)):
            s_arr[p]=(s_arr[p]+upd[p])%26
            s+=chr(s_arr[p]+97)
        
        return s



        # shift={}
        # for i in range(len(shifts)):
        #     if shifts[i][2]==1:
        #         shift[(shifts[i][0],shifts[i][1])]=shift.get((shifts[i][0],shifts[i][1]),0)+1
        #     else:
        #         shift[(shifts[i][0],shifts[i][1])]=shift.get((shifts[i][0],shifts[i][1]),0)-1
        # for j in shift:
        #     for k in range(j[0],j[1]+1):
        #         if shift[j]==0:
        #             continue
        #         else:
        #             offset=ord(s[k])-96
        #             ch_ord=offset+shift[j]
        #             if ch_ord<=0:
        #                 ch_ord=abs(ch_ord)%26
        #                 s=s[:k]+chr(122-ch_ord)+s[k+1:]
        #             else:
        #                 ch_ord%=26
        #                 s=s[:k]+chr(ch_ord+96)+s[k+1:]
        # print(ord('`'))
        # return s
