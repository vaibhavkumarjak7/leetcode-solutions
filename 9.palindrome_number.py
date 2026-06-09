# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        num=str(x)
        rev=num[::-1]

        return num==rev