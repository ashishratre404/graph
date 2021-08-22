# Leetcode: 1197. minimum knight moves

class Solution:
    def minKnightMove(self, x, y):
        steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        seen = set()

        q = [0, [0, 0]]  # [moves, coordinate of position]
        while q:
            moves, coords = q.pop(0)
            if coords[0] == x and coords[1] == y:
                return moves
            
            for s in steps:
                nextStep = (coords[0] + s[0], coords[1] + s[1])

                # this code for to eliminate extra space se are traversing beacuse we are given infinite board of chess
                # suppose our target position is on somewhere at top, so no need to  search traget on bottom
                #------------------------------------------------------------------------------
                if not ((nextStep[0] >= -2 and x >=-2 and nextStep[1] >= -2 and y >= -2) or
                (nextStep[0] <= 2 and x <= 2 and nextStep[1] <= 2 and y <= 2) or
                (nextStep[0] >= -2 and x >=-2 and nextStep[1] <= 2 and y <= 2) or
                (nextStep[0] <= 2 and x <= 2 and nextStep[1] >= -2 and y >= -2)):
                    continue
                #------------------------------------------------------------------------------

                if nextStep not in seen:
                    q.append(moves + 1, nextStep)
                    seen.add(nextStep)
            