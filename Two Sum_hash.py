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
        # hash table optimisation - walk the list once, saving results to a table:
        htable = {}
        for i, item in enumerate(nums):
            if item not in htable:
                htable[item] = i
        
        for item, index in htable.items():
            ideal_item_2 = target - item
            index2 = htable.get(ideal_item_2, None)

            if index2:
                return [index, index2]
            