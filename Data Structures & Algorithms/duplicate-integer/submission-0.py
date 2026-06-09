class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = dict()
        for num in nums:
            if num not in unique_numbers.keys():
                unique_numbers[num] = 1
            else:
                unique_numbers[num]  += 1 
            

        for val in unique_numbers.values():
            if val> 1:
                return True
    
        return False

