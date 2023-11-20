# -*- coding: utf-8 -*-

'''345. Reverse Vowels of a String
Easy
4.2K
2.7K
company
Amazon
company
Apple
company
Bloomberg
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        vowels = 'aeiouAEIOU'
        seperator = ''
        if len(s) ==1:
            return s
        i = 0
        j = len(s)-1
        while i  < len(s):
            while j >= 0:
                if j<=i:
                    return seperator.join(result)
                if s[i] in vowels and s[j] in vowels:
                    result[i]= s[j]
                    result[j] = s[i]
                    i +=1
                    j -= 1
                elif s[i] in vowels and s[j] not in vowels:
                    j -= 1
                elif s[j] in vowels and s[i] not in vowels:
                    i += 1 
                else:
                    i+=1
                    j-=1
        
        

