class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_={}
        out_pt=[]
        for i in range(len(paths)):
            files=paths[i].split(' ')
            dir_=files[0]
            for j in range(1,len(files)):
                brac=files[j].index("(")
                content=files[j][brac:len(files[j])]
                if content not in dict_:
                    dict_[content]=[dir_+'/'+files[j][:brac]]
                else:
                    dict_[content].append(dir_+'/'+files[j][:brac])
        for arr in dict_.keys():
            if len(dict_[arr])>1:
                out_pt.append(dict_[arr])

        return out_pt