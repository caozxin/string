from typing import (
    List,
)

class Solution:

    """
    @param source: 
    @param target: 
    @return: return the index

    description:
    For a given source string and a target string, you should output the first index(from 0) of target string in the source string.If the target does not exist in source, just return -1.
    input:  source = "abcdabcdefg"
            target = "bcd" 
    output = 1

    if no result, return -1. if target = None, return 0. 

    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        n = len(target)
        m = len(source)
        if n <= 0:
            return 0
        if n > m:
            return -1
        for left in range(m): # we first loop into the source
            print("left", left )
            if source[left] == target[0]: # if we find a char from source matching 1st char in target
                
                print("potential match", source[left : left + n])
                potential_match  = source[left : left + n]
                print(len(potential_match))
                if potential_match == target:
                    print("return_result", left)
                    return left
                else:
                    continue
        
        print("return -1")
        return -1
        
        
new_solution = Solution()
source = "abbcdef"
target = "sdf" # expected output = 2
new_solution.str_str(source, target) 