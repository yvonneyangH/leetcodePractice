'''
1679. Max Number of K-Sum Pairs
Medium
2.8K
67
company
Google
company
Apple
company
Amazon
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''
class Solution(object):
    def maxOperations2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict = {}
        count = 0
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num] = 1
        print(dict)
        my_keys = list(dict.keys())
        for key in my_keys:
            matchKey = k-key
            if matchKey == key:
                count+=dict[key]//2
                dict[key]= dict[key]%2
            else:
                if matchKey in dict:
                    if dict[matchKey]>0 and dict[key]>0:
                        minVal = min(dict[matchKey],dict[key])
                        dict[key]-=minVal
                        dict[matchKey]-=minVal
                        count += minVal
        return count
    
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums)-1

        count = 0
        
        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
                r -= 1
                count += 1
        return count

nums = [1,2,3,4]
k= 5
solution = Solution()
print(solution.maxOperations(nums, k))
