#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (35.24%)
# Total Accepted:    115.3K
# Total Submissions: 327.2K
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            # odd
            self.help_fun(s, i, i, dp)
            # even
            self.help_fun(s, i, i + 1, dp)
        res = []
        self.res_fun(s, dp, res, [], 0)
        return res
        
    def help_fun(self, s, left, right, dp):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            dp[left][right] = True
            left -= 1
            right += 1
    
    def res_fun(self, s, dp, res, path, cur):
        if cur == len(dp):
            res.append(path)
            return
        
        for i in range(cur, len(dp)):
            if dp[cur][i] == True:
                self.res_fun(s, dp, res, path + [s[cur:i + 1]], i + 1)
