class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        stack=[]
        for pat in path:
            if pat=='' or pat=='.':
                continue
            elif pat=='..':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(pat)
        return '/'+'/'.join(stack)