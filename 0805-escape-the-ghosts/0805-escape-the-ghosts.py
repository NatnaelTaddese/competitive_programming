class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def dist(p1,p2):
            return abs(p1[0] - p2[0])  + abs(p1[1] - p2[1])
        # measure_distance

        # Initialize nearest_ghost with a large value
        player_distance = float(dist([0,0], target))

        for ghost in ghosts:
            ghost_distance = dist(ghost, target)
            if player_distance >= ghost_distance:
                return False
        
        return True




        # game_over = False
        # won = False
        # player = [0, 0]

        # while(not game_over):

        #     # move ghots
        #     for ghost in ghosts:
        #         if ghost[0] == target[0]:
        #             if ghost[1] == target[1]:
        #                 # ghost won
        #                 won = False
        #                 game_over = True
        #                 break
                    
        #             elif ghost[1] < target[1]:
        #                 ghost[1] += 1
        #             else:
        #                 ghost[1] -= 1
                
        #         else:
        #             if ghost[0] < target[0]:
        #                 ghost[0] += 1
        #             else:
        #                 ghost[0] -= 1
            
        #     # move_player

        #     if player[0]== target[0] and player[1] == target[1]:
        #         # game won
        #         game_over = True
        #         won = True
        #         break

        #     else:





        