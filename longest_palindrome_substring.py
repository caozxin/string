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