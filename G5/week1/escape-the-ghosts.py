class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x_turn=abs(0-target[0])
        y_turn=abs(0-target[1])
        turn=(x_turn+y_turn)
        for i in range(len(ghosts)):
            x_dis=abs(ghosts[i][0]-target[0])
            y_dis=abs(ghosts[i][1]-target[1])
            near_ghost=x_dis+y_dis
            if near_ghost<=turn:
                return False
        return True
