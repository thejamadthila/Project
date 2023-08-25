def selection_sort(array):
  length=len(array)
  for i in range(length-1):
    minindex=i
    for j in range(i+1,length):
     if array[j]<array[minindex]:
      minindex=j
    array[i],array[minindex]=array[minindex],array[i]
  return array
array=[30,45,20,16,25,1]
print("the unsorted list is:",array)
print("the sorted array is:",selection_sort(array))
