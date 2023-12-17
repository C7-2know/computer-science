class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_={}
        for i in cpdomains:
            web_visit=i.split(' ')
            time=int(web_visit[0])
            site=web_visit[1].split('.')
            for j in range(len(site)):
                name='.'.join(site[len(site)-1-j:])
                dict_[name]=dict_.get(name,0)+time
        arr=[]
        for key,val in dict_.items():
            arr.append(f"{val} {key}")
        return arr
            
