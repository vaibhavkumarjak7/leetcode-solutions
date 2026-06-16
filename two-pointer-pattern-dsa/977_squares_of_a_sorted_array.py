# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100]

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []

        for num in nums:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)

        if len(neg)==0:
            for i in range(len(pos)):
                pos[i] = pos[i]*pos[i]
            return pos

        if len(pos)==0:
            for i in range(len(neg)):
                neg[i] = neg[i]*neg[i]
            neg.reverse()
            return neg

        arr = []

        for i in range(len(pos)):
            pos[i] = pos[i]*pos[i]
        
        for i in range(len(neg)):
            neg[i] = neg[i]*neg[i]

        neg.reverse()

        i = 0
        j = 0