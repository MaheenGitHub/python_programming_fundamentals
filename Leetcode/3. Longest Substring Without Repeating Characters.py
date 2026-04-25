"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
 
s = "abc"
count = 0
max_count = [0]

print("My approach")
result = []
for i in range(0, len(s)) :
    result.append(s[i])
    for j in range(i+1,len(s)) :
        if (s[j] not in result) :
            result.append(s[j])
        else :
            break
    
    count = len(result)
    max_count.append(count)
    print(result)
    result.clear()
    

print(max(max_count))
    
print("Sliding window technique")
left = 0
max_length = 0
char_set = set()

for right in range(len(s)) :
    while s[right] in char_set :
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])
    max_length= max(max_length , right - left + 1)
print(max_length)



"""
code i submitted on leetcode

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0 
        result = []
        max_count = [0]

        for i in range (0 , len(s)) :
            result.append(s[i])
            for j in  range (i+1 , len(s)) :
                if (s[j] not in result ) :
                    result.append(s[j])
                else : 
                    break
            count = len(result)
            max_count.append(count)
            result.clear()
        return (max(max_count))

"""