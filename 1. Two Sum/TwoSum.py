class Solution:
    ### 
    # twoSum: 
    # @sum return the two values equal to target
    # @param nums: values to be checked, ints
    # @param target: value that that two ints from nums must equal to
    # return List[int]: two values that add up to target
    # ###
    def hashtwoSum(self, nums: List[int], target: int) -> List[int]:
        ### 
        # We can iterate through the array once, and for each element, 
        # check if the target minus the current element exists in the hash table. 
        # If it does, we have found a valid pair of numbers.
        #  If not, we add the current element to the hash table.
        # ###
        
        #empty map (hashtable/unordered map)
        numMap = {}
        n = len(nums)
        
        #iterate using n
        for i in range(n):
            # the complement from the current nums value is saved,
            complement = target - nums[i]
            # if present in the map, means that the current value (nums[i]) + complement is equal to target 
            if complement in numMap:
                return [numMap[complement], i]
            # otherwise save the current value to map
            numMap[nums[i]] = i

        return []  # No solution found
###
# Example: 
# nums: [3,2,4]
# target: 6
# 
# n = 3
# loop pass 0:
# complement = 6 - 3 = 3
# no return
# numMap[3] = 0
# 
# loop pass 1:
# complement = 6 - 2 = 4
# no return
# numMap[4] = 1
# 
# loop pass 2:
# complement = 6 - 4 = 2
# 4 is in numMap
# return 1,2 (numMap[4] = 1, i = 2)
#  ###