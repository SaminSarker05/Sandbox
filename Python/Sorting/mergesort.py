def mergesort(array):
  if len(array) <= 1: return array
  mid = len(array) // 2
  l = mergesort(array[:mid])
  r = mergesort(array[mid:])
  return merge(l, r)

def merge(a1, a2):
  if not a1 and not a2: return []
  if not a1: return a2
  if not a2: return a1
  p, q = 0, 0
  res = []
  while p < len(a1) and q < len(a2):
    if a1[p] < a2[q]: 
      res.append(a1[p])
      p += 1
    elif a1[p] > a2[q]:
      res.append(a2[q])
      q += 1
    else:
      res.append(a2[q])
      res.append(a2[q])
      p += 1
      q += 1

  while p < len(a1):
    res.append(a1[p])
    p += 1
  
  while q < len(a2):
    res.append(a2[q])
    q += 1
  return res

if __name__ == '__main__':
  arr = [9, 8, 7, 6, 5, 4]
  print(mergesort(arr))

  arr = [0, 1]
  print(mergesort(arr))

  arr = [100]
  print(mergesort(arr))

  arr = [1, 4, 5 , 7, 1, 3, 4]
  print(mergesort(arr))
