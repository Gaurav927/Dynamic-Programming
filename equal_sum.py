from functools import lru_cache
def isEqualSum(nums):
    target = sum(nums)
    
    if target%2:
        return False
    
    @lru_cache(maxsize=None)
    def helper(index, target):
        
        if target==0:
            return True
        
        if target<0 or index>=len(nums):
            return False
        
        return helper(index+1, target - nums[index]) or helper(index+1, target)
    
    return helper(0, target//2)


print(isEqualSum([2, 3, 5, 6]))