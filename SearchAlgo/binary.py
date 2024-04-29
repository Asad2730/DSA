from bubbleSort import bubble_sort

def binary(arr,target):
  arr = bubble_sort(arr)
  left,right = 0,len(arr)-1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid] :
        left = mid + 1
    else:
       right = mid - 1    
  return None     





