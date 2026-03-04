class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dc={}
        for str_ in strs:
            key=''.join(sorted(str_))
            if key not in dc:
                dc[key]=[]
            dc[key].append(str_)
        return list(dc.values())