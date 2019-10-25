# Create a function named double_index that has two parameters named lst and index.
# The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.
# If index is not a valid index, the function should return the original list.
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    lst[index] = lst[index] * 2
    return lst

# test the function
print(double_index([2, 1, -5, 12], 2))
