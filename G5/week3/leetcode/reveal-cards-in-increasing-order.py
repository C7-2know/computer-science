class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=deque()
        for i in deck:
            if queue:
                back=queue.pop()
                queue.appendleft(back)
            queue.appendleft(i)
        return list(queue)
        
        
        
        
        
        
        



        # deck.sort(reverse=True)
        # que=deque()
        # for i in deck:
        #     if que:
        #         prev=que.pop()
        #         que.appendleft(prev)
        #         que.appendleft(i)
        #     else:
        #         que.append(i)
        # return list(que)


















        # deck.sort(reverse=True)
        # q=deque([deck[0]])
        # for i in range(1,len(deck)):
        #     back=q.pop()
        #     q.appendleft(back)
        #     q.appendleft(deck[i])
        # return list(q)        