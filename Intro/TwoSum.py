def twoSum(self, nums: List[int], target: int) -> List[int]:
    while i < len(nums):
    j=i+1
    while j < len(nums):
        if mylist[j]+nums[i] == t:
            print("Elements are "+str(nums[j])+ " and "+str(nums[i]))
            return i,j
        else:
            j= j+1
    i=i+1

mylist = [1, 2, 3, 4, 5, 6]
print(len(nums))