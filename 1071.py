"""
1071. Greatest Common Divisor of Strings
Easy
4.1K
787
company
Amazon
company
Yahoo
company
Apple
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        result = ""
        if len(str1)==len(str2):
            if str1==str2:
                return str1
            else:
                return result
        elif len(str1)>len(str2):
            testStr = str2
            targetStr = str1
        else:
            testStr = str1
            targetStr = str2
        for x in range(len(testStr)):
            tempStr = testStr[0:x+1]
            if len(targetStr)%(x+1) == 0 and len(testStr)%(x+1)==0:
                StrCompareTarget = len(targetStr)//(x+1)*(tempStr)
                StrCompareTest = len(testStr)//(x+1)*(tempStr)
                if StrCompareTarget == targetStr and StrCompareTest == testStr:                   
                    result = tempStr

        return result

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"   
solution = Solution()
print(solution.gcdOfStrings(str1,str2))   
            
            
            
            
        
        
