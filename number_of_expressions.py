import unittest
from functools import lru_cache

class TestCountExpressions(unittest.TestCase): 
    def test_1_simple(self):
        self.assertEqual(count_expressions([2, 1, 1], 2), 2)
        print("Working 1")
        self.assertEqual(count_expressions([1, 2, 2, 3, 3], 7), 2)
        print("Working 2")
        self.assertEqual(count_expressions([1,2, 2, 3, 1], 3), 3)
        print("Working 3")



def count_expressions(nums, target):    
    @lru_cache(maxsize=None)
    def helper(index, paritial_sum):
        if index==len(nums):
            if paritial_sum==target:
                return 1
            return 0
        
        count_neg = helper(index+1, paritial_sum-nums[index])
        count_pos = helper(index+1, paritial_sum+nums[index])
        
        return count_neg+count_pos
    
    
    return helper(1, nums[0])

a = TestCountExpressions()
a.test_1_simple()
    