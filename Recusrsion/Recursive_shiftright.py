def shift_right(arr, index=None, last=None):
    if index is None:
        index = len(arr) - 1
        last = arr[-1]

    if index == 0:
        arr[0] = last
        return arr

    arr[index] = arr[index - 1]
    return shift_right(arr, index - 1, last)


print('original')
print([1,2,3,4])
print("shift right")
print(shift_right([1, 2, 3, 4]))  # output: [4, 1, 2, 3]
print(shift_right([1]))