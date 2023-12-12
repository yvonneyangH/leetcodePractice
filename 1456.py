# -*- coding: utf-8 -*-
'''

1456. Maximum Number of Vowels in a Substring of Given Length
Medium
3.2K
109
company
Amazon
company
Apple
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

'''

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        currSubstring = s[0:k]
        vowel = 'aeiou'
        currCount = 0
        
        for ele in currSubstring:
          if ele in vowel:
            currCount += 1
        maxCount = currCount
        print("line 54 maxCount:",maxCount)
        for i in range(k,len(s),1):
          if s[i-k] in vowel:
            currCount -= 1
          if s[i] in vowel:
            currCount += 1
          print('line64 currCount:',currCount,"s[i-k]:",s[i-k],"s[i]:",s[i])
          if currCount > maxCount:
            maxCount = currCount
        return maxCount
s = "weallloveyou"
k = 7
solution = Solution()
print(solution.maxVowels(s, k))
