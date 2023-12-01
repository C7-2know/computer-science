class Solution:
    def interpret(self, command: str) -> str:
        out=''
        i=0
        while i<len(command):
            st=''
            if command[i]=='G':
                st='G'
            elif command[i]=='(' and command[i+1]==')':
                st='o'
                i+=1
            elif command[i]=='':
                continue
            else:
                st='al'
                i+=3
                

            i+=1
            out+=st
            print(out,i)

        return out
            