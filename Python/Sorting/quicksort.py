def quicksort(array):
  if len(array) <= 1: return array
  pivot = array.pop()
  left = []
  right = []
  for num in array:
    if num <= pivot: left.append(num)
    else: right.append(num)
  
  return quicksort(left) + [pivot] + quicksort(right)

if __name__ == '__main__':
  arr = [9, 8, 7, 6, 5, 4]
  print(quicksort(arr))

  arr = [0, 1]
  print(quicksort(arr))

  arr = [100]
  print(quicksort(arr))

  arr = [1, 4, 5 , 7, 1, 3, 4]
  print(quicksort(arr))
