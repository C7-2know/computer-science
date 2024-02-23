class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                st=stack.pop()
                str_=''
                while st!='[':
                    str_=st+str_
                    st=stack.pop()
                num=stack.pop()
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                # print(num)
                stack.append(str_*int(num))
        return ''.join(stack)