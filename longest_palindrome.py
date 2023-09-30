from collections import Counter
import math
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built

    description: Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

    Input : s = "abccccdd"
    Output : 7
    Explanation :
    One longest palindrome that can be built is "dccaccd", whose length is `7`.

    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        counter = Counter(s)
        print(counter) # counter acts as a dictionary here
        palindrome_length = 0
        additional_length = 0

    

        for each_char in counter:
            if len(counter) == 1:
                print(counter[each_char])
                return counter[each_char]
            print(each_char, counter[each_char])
            number = (counter[each_char] // 2)
            if counter[each_char] % 2 != 0: # odd number
                # print(counter[each_char] /2)
                math.floor(number)
                print("no round down", number)
                additional_length = 1
                    # print(additional_length)
                
            elif counter[each_char] % 2 == 0:  # if it is even number

                # print((counter[each_char] // 2))
                # number = counter[each_char] 
                math.floor(number)
                print("round down", number)
                # print("counter[each_char]", counter[each_char])
                
            palindrome_length += number * 2

        print("palindrome_length", palindrome_length + additional_length)
        return palindrome_length + additional_length

new_solution = Solution()
s01 = "abccccddBBAC"
s02 = "aaabccccdd"
s = "abccccdd"
s05 = "aaa"
s06 = "dbcbaccdccbdbcabbcbcadaadcacaaabaabadbdcdaccbccabbbdcadacbcdbabadcdcdaddbabbabdcacbaddadcbaccdcdcdacabababdababdbadadabdacbdddcdbbabcabcbaabbcacddddaadaabbcdccddabcadcaaccbbdbcbbbdaabdadbaaaddcbabdbbabcaabdbbcaabdbcbcabababddcacacbadabdacddccaccaacdacddcbbadcabcddacaadddbbaadacddbdacdcd"
new_solution.longest_palindrome(s)