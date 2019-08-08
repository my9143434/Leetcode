class Solution:
    def removeDuplicates(self, nums):
        count = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[count-2]:    # 0,1,2,3,4
                nums[count] = nums[i]
                count += 1
        print(count)
        print(len(nums))
        return min(count, len(nums))


num_input = [1, 2, 3, 4, 4, 4, 4, 5,5,5,5,5,5,5,5,5]


first = Solution()
result = first.removeDuplicates(num_input)
print("result:", result)
