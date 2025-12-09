class Solution:
    def convert(self, s: str, numRows: int) -> str:
        out=""
        zig_len = 2*(numRows-1) if numRows > 1 else numRows
        zigs =[]
        idx = 0
        for _ in range(len(s)//zig_len + 1):
            if idx+zig_len > len(s):
                zigs.append(s[idx:])
            else:
                zigs.append(s[idx:idx+zig_len])
            idx+=zig_len
        for i in range(numRows):
            for zig in zigs:
                if i>=len(zig):
                    continue
                out+= zig[i]
                if i!=0 and i!=numRows-1:
                    if len(zig)<= zig_len-i:
                        continue
                    out+=zig[zig_len-i]
                print(out)

        return out
