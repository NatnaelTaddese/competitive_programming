class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
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

        