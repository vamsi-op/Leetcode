from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        
        while True:
            if all(nums[i] >= nums[i - 1] for i in range(1, len(nums))):
                break

            min_sum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            res += 1

        return res
