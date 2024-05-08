class RecentCounter(object):

    def __init__(self):
        self.counter = 0
        self.queue = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        self.counter += 1
        while (t - self.queue[0]) > 3000:
            self.queue.pop(0)
            self.counter -= 1

        return self.counter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)