class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, j in enumerate(nums):
            if j != val:
                nums[count] = j
                count += 1
        return count


num_input = [1, 2, 3, 4, 4, 4, 4, 5]
val_input = 4


first = Solution()
result = first.removeElement(num_input, val_input)
print("result:", result)