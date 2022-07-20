class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = collections.Counter(tasks)
        maxFreq, maxCount = 0, 0
        for key in counts:
            if counts[key] == maxFreq:
                maxCount += 1
            elif counts[key] > maxFreq:
                maxCount = 1
                maxFreq = counts[key]
        
        partCount = maxFreq - 1
        partLength = n - maxCount + 1 
        empty = partCount*partLength
        tasks_left = len(tasks) - maxFreq*maxCount
        idles = max(0, empty - tasks_left)
        
        return len(tasks)+idles