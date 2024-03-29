class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DFS idea
        # use visited to track visited nodes, without using recursive methods
        res = 0
        visited = set()
        for i in range(len(nums)):
            if i not in visited:
                count = 0
                while i not in visited:
                    count += 1
                    visited.add(i)
                    i = nums[i]
                res = max(res, count)
        return res
