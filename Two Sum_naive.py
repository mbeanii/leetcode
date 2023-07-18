class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs:
            nums (List[int]): 
            target (int)    : The number to be summed to

        Outputs:
            A list containing two elements - unique indices of the two numbers in `nums` whose sum is `target.`
        
        Constraints:
            1) Each input will have exactly one solution.
            2) Do not use the same element twice.

        Raises:
            - Don't need to error check due to constraint #1 above
        """
        # Naive solution
        # Walk the list twice, summing all possible combinations of numbers.
        for i, first_item in enumerate(nums):
            for j, second_item in enumerate(nums):
                # Constraint #2
                if i == j:
                    continue
                if first_item + second_item == target:
                    return [i, j]
                