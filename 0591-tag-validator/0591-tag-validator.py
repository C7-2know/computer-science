class Solution:
    def isValid(self, code: str) -> bool:
        open_='<'
        close='</'
        stack=[]
        count=0
        i=0
        while i <len(code):
            if code[i]==open_:
                if i+1<len(code) and code[i+1]=='/':
                    #  this is closing
                    i+=2
                    tag=''
                    while i<len(code) and code[i]!='>':
                        tag+=code[i]
                        i+=1
                    if not tag.isupper():
                        return False
                    if not stack or stack[-1]!=tag:
                        return False
                    stack.pop()
                    i+=1
                elif i+8<len(code) and code[i:i+9]=='<![CDATA[':
                    # this is c_data
                    i+=9
                    while i+2<len(code) and code[i:i+3]!=']]>':
                        i+=1
                    if i+2>=len(code) or not stack:
                        return False
                    i+=3
                else:
                    tag=''
                    i+=1
                    while  i<len(code) and code[i]!='>':
                        tag+=code[i]
                        i+=1
                    if len(tag)>9 or tag=='':
                        return False
                    # check uppercase
                    if not tag.isupper() or not tag.isalpha():
                        return False
                    if len(stack)==0:
                        count+=1
                    stack.append(tag)
                    i+=1
            else:
                if not stack:
                    return False
                i+=1
        return True if len(stack)==0 and count==1 else False
            

                    

