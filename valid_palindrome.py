from collections import Counter
import math

class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    
    Description: Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    Please note: 
    1) this question asks if a input string is a palindrome, if you can only at most remove one character. 
    2) this is a two pointers question.

    Input: s = "aba"
    Output: true
    Explanation: Originally a palindrome.

    """
    def valid_palindrome01(self, s: str) -> bool:
        # Write your code here

        input_string = s
        if len(input_string) <= 0:
            return False
        
        n = len(input_string)
        if n == 2:
            return True
        
        left, right = 0 , n -1
        only_pass = 0

        while left <= right:
            if input_string[left] == input_string[right]:
                # print("matching starts")
                if left == right:
                    return True
                left += 1
                right -= 1
            else:
                if only_pass == 0:
                    only_pass = 1
                else:
                    return False
            
    def valid_palindrome(self, s: str) -> bool:
        # Write your code here
        #there could be 2 levels of validation
        
        
        input_string = s
        if len(input_string) <= 0:
            return False
        
        n = len(input_string)
        if n == 2:
            return True
        
        # 1st round of validation 
        if self.is_palindrome(input_string) == True:
            return True

        for idx in range(n):

            new_input = input_string[:idx] + input_string[idx+1:]
            if self.is_palindrome(new_input) == True:
                return True
            
        
        return False
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def valid_palindrome03(self, s: str) -> bool:
        if not s:
            return False

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # If the characters at the current positions don't match,
                # try removing one of them and check if the resulting substring is a palindrome.
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


new_solution = Solution()
s = "aaa" #return True
s02 = "abc" #return False
s03 = "ab" #return True
s05 ="ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno" #return False
s06 = "abca"  # return True
samples = [s, s02, s03, s05, s06]
for each_sample in samples:
    result = new_solution.valid_palindrome(each_sample)
    print("result", result)

# result = new_solution.valid_palindrome(s06)
# print("result", result)
