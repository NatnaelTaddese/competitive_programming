class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        # Brute force method:

        # no_losses = set()
        # only_one_lose = set()

        # for i in range(len(matches) ):

        #     loss = 0
        #     only_one = 0

        #     for j in range(0, len(matches)):
        #         if matches[i][0] == matches[j][1]:
        #             loss += 1
        #         if matches[i][1] == matches[j][1]:
        #             only_one += 1

        #     if loss == 0:
        #         no_losses.add(matches[i][0])
            
        #     if only_one == 1:
        #         only_one_lose.add(matches[i][1])
        
        # no_losses = sorted(no_losses)
        # only_one_lose = sorted(only_one_lose)

        # # no_losses = set(no_losses)
        # # only_one_lose = set(only_one_lose)
        
        # return[no_losses,only_one_lose]


        wins = dict()
        losses = dict()

        for winner, loser in matches:
            if winner in wins:
                wins[winner] += 1
            else:
                wins[winner] = 1
            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1
            
        no_loss = []
        only_one_loss = []

        for player in wins:
            if player not in losses:
                no_loss.append(player)

        for player, value in losses.items():
            if value == 1:
                only_one_loss.append(player)
    
        no_loss.sort()
        only_one_loss.sort()
        return [no_loss, only_one_loss]
        