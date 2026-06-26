# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue

            target = -1 * nums[i]
            left = i + 1
            right = len(nums)-1

            while(left<right):
                sum = nums[left] + nums[right]
                if sum == target:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while(left<right and nums[left]==nums[left-1]):
                        left += 1
                    while(left<right and nums[right]==nums[right+1]):
                        right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return triplets    