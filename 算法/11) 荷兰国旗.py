class HeLanGuoQi:
    def solution(self,nums):
        left = 0
        right = len(nums)-1
        cursor = 0
        while cursor<=right:
            if nums[cursor] == 0:
                nums[cursor],nums[left] = nums[left],nums[cursor]
                left += 1
                cursor += 1
            elif nums[cursor] == 1:
                cursor += 1
            else:
                nums[cursor], nums[right] = nums[right], nums[cursor]
                right -= 1
        return nums
a = HeLanGuoQi()
c = a.solution([1,1,2,1,2,0])
print(c)

