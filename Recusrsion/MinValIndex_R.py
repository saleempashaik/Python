def findMinIndex(array, index=0, MinIndex=None) -> int:
    if index == len(array):
        return MinIndex
    if MinIndex == None or array[index] < array[MinIndex]:
        MinIndex = index
    return findMinIndex(array,index+1,MinIndex)

Array = [1,0,9,-4,3]
Empty_Array= []
print(findMinIndex(Empty_Array,0))
print((findMinIndex(Array,0)))