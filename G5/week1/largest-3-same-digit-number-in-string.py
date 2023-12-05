class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num='0'
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if len(max_num)==1:
                    max_num=num[i:i+3]
                if int(num[i:i+3])>int(max_num):
                    max_num=num[i:i+3]
        if len(max_num)==1:
            return ""
        return str(max_num)