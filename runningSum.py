class Solution:
    """
    This function provides a method to compute the running sum of a list of integers.
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        This function computes the running sum of a list of integers.
        The running sum at each index i is defined as the sum of all elements from index 0 to index i.
        
        Args:
        nums (List[int]): A list of integers.
        
        Returns:
        List[int]: A list where each element at index i contains the sum of elements from index 0 to i in the original list.
        
        Example:
        If nums = [1, 2, 3, 4], the function returns [1, 3, 6, 10].
        
        """

        # Start a loop from index 1 to the last index of the list
        # We start at 1 because there's no previous element to sum for index 0
        for i in range(1, len(nums)):  # Loop through the list starting from the second element (index 1)
            # Update the current element by adding the value of the previous element
            # This creates a cumulative sum (running sum) as we move through the list
            nums[i] += nums[i - 1]

        # After the loop has processed all elements, return the modified list, which now contains the running sums
        return nums
    """
    Step-by-Step Process:
    Given nums = [1, 2, 3, 4]:
    
    1. At i = 1:
        nums[1] = nums[1] + nums[0]
        nums = [1, 3, 3, 4]  # 2 (at index 1) is updated to 3 (1 + 2).
    
    2. At i = 2:
        nums[2] = nums[2] + nums[1]
        nums = [1, 3, 6, 4]  # 3 (at index 2) is updated to 6 (3 + 3).
    
    3. At i = 3:
        nums[3] = nums[3] + nums[2]
        nums = [1, 3, 6, 10]  # 4 (at index 3) is updated to 10 (4 + 6).
    
    The final result is [1, 3, 6, 10].
    """