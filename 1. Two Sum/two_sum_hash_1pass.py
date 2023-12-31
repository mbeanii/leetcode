from typing import List

class Solution:
    def __init__(self):
        self.htable = {}

    def find_index2(self, target: int, item: int) -> int:
        """ Returns the index of target - item if it is found in htable """        
        ideal_item_2 = target - item
        return self.htable.get(ideal_item_2)
            
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
        # hash table optimisation - walk the list once, looking for a solution in htable and
        # returning if one is found; memoizing otherwise:
        for i, item in enumerate(nums):
            j = self.find_index2(target, item)
            if j:
                return [i, j]
            self.htable[item] = i
