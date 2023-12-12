'''
643. Maximum Average Subarray I
Easy
3.2K
264
company
Apple
company
Adobe
company
Facebook
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max = float('-inf')
        for i in range(k-1,len(nums),1):
            copyList = nums[i-k+1:i+1]
            print(copyList)
            currVal = sum(copyList)
            if currVal > max:
                max = currVal
            print(max)
            print(k)
        return max/k
nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))