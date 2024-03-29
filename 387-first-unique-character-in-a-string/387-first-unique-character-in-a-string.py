class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1