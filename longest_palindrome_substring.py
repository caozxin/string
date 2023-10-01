class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s: str) -> str:
        # write your code here
        input_string = s
        print("input_string", input_string)
        n = len(input_string)

        if n <= 0:
            return None
        
        left, right = 0, n-1
        
        # print("new_palindrome", new_palindrome, len(new_palindrome))
        #start 1st loop:
        while left <= right:
            new_palindrome = [" "] *n
            print(left, input_string[left],right, input_string[right])

            if input_string[left] == input_string[right]: 
                new_palindrome[left], new_palindrome[right] = input_string[left], input_string[right]
                print("new_palindrome", new_palindrome, len(new_palindrome))
                # when you find the 1st match, you start the 2nd loop: --> the excit of the 2nd loop is left +=1 & new_palindrome = []
                
                while left <= right: 
                    prev_left = left

                    if input_string[left] == input_string[right]: 
                        new_palindrome[left], new_palindrome[right] = input_string[left], input_string[right]
                        if left == right:
                            # new_palindrome.remove(" ")
                            result = "".join(each_letter.replace(" ", "") for each_letter in new_palindrome)
                            # result.split(" ")
                            # return result, len(result)
                            
                            return result
                        else:
                            left += 1
                            right -= 1
                        
                    else:
                        left = prev_left + 1
                        right = n - 1
                        break


            else:
                right -= 1

        result = "".join(each_letter.replace(" ", "") for each_letter in new_palindrome)
        return result
    
    def longest_palindrome02(self, s: str) -> str:
        # write your code here
        input_string = s
        print("input_string", input_string)
        n = len(input_string)

        if n <= 0:
            return None
        
        left, right = 0, n-1

        palindrome_substring = []
        
        # print("new_palindrome", new_palindrome, len(new_palindrome))

        # while left <= right:
        while left <= right:  #this is to check left pointer
            new_palindrome = [" "] * (right - left + 1) # reset new_palindrome
            print(left, input_string[left],right, input_string[right])

            
            if input_string[left] == input_string[right]: # we start testing if palindrome inside
                
                if self.is_palindrome(input_string,left,right, new_palindrome):
                    substring = self.is_palindrome(input_string,left,right, new_palindrome)
                    palindrome_substring.append(substring)
                    
                #reset left and right
                left += 1
                right = n - 1 # going back to 1st loop

            # elif left == right:
            #     break
            else:
                right -= 1
        
        left, right = 0, n-1

        while left <= right:  #this is to check left pointer
            new_palindrome = [" "] * (right - left + 1) # reset new_palindrome
            print(left, input_string[left],right, input_string[right])

            
            if input_string[left] == input_string[right]: # we start testing if palindrome inside
                
                if self.is_palindrome(input_string,left,right, new_palindrome):
                    substring = self.is_palindrome(input_string,left,right, new_palindrome)
                    palindrome_substring.append(substring)
                    
                #reset left and right
                left = 0 
                right -= 1 # going back to 1st loop

            # elif left == right:
            #     break
            else:
                left += 1
                

        # result = "".join(each_letter.replace(" ", "") for each_letter in new_palindrome)
        # return result
        max_length = 0 
        for each_substring in palindrome_substring:
            curr_length = len(each_substring)
            if curr_length >= max_length:
                max_length = curr_length
                result = each_substring

        updated_result = "".join(each_letter.replace(" ", "") for each_letter in result)
        return updated_result

        # for each_substring in 
    
    
    def is_palindrome(self, input_string: str, left: int, right: int, new_palindrome) -> str: # return new_palindrome if it is true 
        
        new_input = input_string[left: right+1]
        m = len(new_input)
        start, end = 0 , m-1

        while start <= end:

            if new_input[start] == new_input[end]: 
                new_palindrome[start], new_palindrome[end] = new_input[start], new_input[end]
                start += 1
                end -= 1
                
            else:
                return False
        
        return new_palindrome

    def longest_palindrome_dynamic_programming(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # Create a table to store if substrings are palindromes
        is_palindrome = [[False] * n for _ in range(n)]

        start = 0  # Start index of the longest palindrome found so far
        max_length = 1  # Length of the longest palindrome found so far

        # All substrings of length 1 are palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start:start + max_length]

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

new_solution = Solution()
s01 = "abcdzdcab"
s02 = "cdzdc"
s03 = "bb"
s05 = "abb"
s06 = 'aaabaaaa'
s07 = 'abaa'
result = new_solution.longest_palindrome02(s03)
print("result", result)

# for s in [s01, s02, s03]:
#     result = new_solution.longest_palindrome(s)
#     print("result", result)