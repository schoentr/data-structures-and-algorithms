def insertShiftArray(arr, value):
    
    mid = len(arr) // 2
    new_arr = []
    
    for i in range(0, mid):
        new_arr.append(arr[i])
    
    new_arr.append(value)
    
    for i in range(mid, len(arr)):
        new_arr.append(arr[i])
    
    return new_arr

test = [1, 2, 3, 4, 5]
print(test)
print(insertShiftArray(test, 8))
test2 = [1,2,3,4]
print(test2, 8)
print(insertShiftArray(test2, 8))
