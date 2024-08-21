class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = Counter(tasks)

        max_freq = max(task_counts.values())
        tasklist = list(task_counts.values())
        max_freq_count = tasklist.count(max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(intervals, len(tasks))
