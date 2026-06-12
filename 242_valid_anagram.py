# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s==t