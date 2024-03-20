class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """

        players.sort()
        trainers.sort()
        # trainers = sorted(trainers, reverse=True)
        matches = 0

        # left = 0
        # right = len(trainers) - 1

        # while(left <= len(players) or right > -1):
        #     if players[left] > trainers[right]:
        #         break
        #     elif 
        # return matches

        # n = min(len(players), len(trainers))
        # for i in range(n):
        #     if players[i] <= trainers[i]:
        #         matches += 1
        #     else:
        #         break
        
        # return matches

        

        player = 0
        trainer = 0

        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                matches += 1
                player += 1
                trainer += 1
            else:
                trainer += 1

        return matches
        