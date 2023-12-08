class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_={order[i]:i for i in range(len(order))}

        for i in range(len(words)-1):
            for h in range(len(words[i])):
                if h==len(words[i+1]):
                    return False
                # elif h>len(words[i+1]):
                #     return False 
                elif dict_[words[i][h]]>dict_[words[i+1][h]]:
                    return False
                elif dict_[words[i][h]]<dict_[words[i+1][h]]:
                    break
        return True

        # max_word=words[0]
        # for i in range(len(max_word)):
        #     prev_index=dict_[words[0][i]]
        #     j=0
        #     while j<len(words):
        #         if len(words[j])>len(max_word):
        #             max_word=words[j]
        #         if i>len(words[j])-1:
        #             return False
        #         elif prev_index<dict_[words[j][i]]:
        #             words.pop(j)
        #         elif dict_[words[j][i]]<prev_index:
        #             return False
        #         else:
        #             j+=1
                
        # if len(words)>1:
        #     print(words)
        #     return False
        # return True

        