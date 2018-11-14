class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        start = 0
        temp = dict()
        for i in range(len(s)):
            start = max(start, temp.get(s[i], -1) + 1)
            l = max(l, i - start + 1)
            temp[s[i]] = i
        return l