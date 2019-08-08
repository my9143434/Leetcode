# 27


class Solution:
    def removeElement(self, nums, val):  # self is temporarily replace of object itself
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


num_input = [1, 2, 3, 4, 4, 4, 4, 5]
print(type(num_input))
val_input = 4


first = Solution()
result = first.removeElement(num_input, val_input)
print("result:", result)
