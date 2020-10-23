class Solution:
    def twoSum(self, nums, target: int):
        lett = 0
        right = len(nums) - 1
        while lett < right:
            if nums[lett] + nums[right] == target:
                return lett, right
            elif nums[lett] + nums[right] > target:
                right -= 1
            else:
                lett += 1
        return None

a = Solution()
c = a.twoSum([1,2,3,4,5],7)
print(c)