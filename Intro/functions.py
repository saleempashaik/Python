def twoSum( nums: [int], target: int) -> [int]:
    i = 0
    while i < len(nums):
        j = i + 1
        print(f'in {i} loop with j value {j}')
        while j < len(nums):
            print(f' j value is {j}')
            if nums[j] + nums[i] == target:
                return i, j
            j = j+ 1
        i = i+ 1
    return []

print(twoSum([1,2,3,4],6))