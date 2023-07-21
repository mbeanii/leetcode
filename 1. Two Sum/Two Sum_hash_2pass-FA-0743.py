from typing import List

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
        # hash table optimisation - walk the list once (first pass), saving results to a dict of lists:
        htable = {}
        for i, item in enumerate(nums):
            if item not in htable:
                htable[item] = [i]
            else:
                htable[item].append(i)
        
        # Walk the dict (second pass) - look for a solution
        for item, index_list in htable.items():
            index1 = index_list[0]
            ideal_item_2 = target - item
            for index2 in htable.get(ideal_item_2, []):
                if index2 != index1:
                    return [index1, index2]
                
            
test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test_nums2 = [2, 2]
test_target = 25
test_target2 = 4
solution = Solution()
print(solution.twoSum(test_nums, test_target))
print(solution.twoSum(test_nums2, test_target2))