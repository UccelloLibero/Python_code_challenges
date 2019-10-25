# 1.
# Create a function named double_index that has two parameters named lst and index.
# The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.
# If index is not a valid index, the function should return the original list.
# Example: double_index([1, 2, 3, 4] 1) will return [1, 4, 3, 4] because the number at the index 1 was doubled

def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    lst[index] = lst[index] * 2
    return lst

# test the function
print(double_index([2, 1, -5, 12], 2))


# 2.
# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
# Example: remove_middle([1, 2, 3, 4, 5, 6, 7], 1, 5) returns [1, 7] because indices 1,2,3,4,5 have been removed
def remove_middle(lst, start, end):
  first_half = lst[:start]
  second_half = lst[end+1:]
  return first_half + second_half

# test the function
print(remove_middle([5, 11, 25, 17, 100, -99], 1, 3))


# 3.
# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#test the function
print(more_than_n([2, 5, 6, 1, 3, 5, 3, 2], 5, 3)) # returns False


# 4.
# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  elif lst.count(item1) == lst.count(item2):
    return item1

# test the function
print(more_frequent_item([2, 7, 1, 11, 9, 7, 7, 7, 11], 7, 11)) # output is 7


# 5.
# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  if (len(lst) % 2) != 0:
    return lst[((len(lst) - 1) // 2)]
  elif (len(lst) % 2) == 0:
    return (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2


# test the function
print(middle_element([5, 2, -10, -4, 4, 5])) # output -7


# 6.
# Write a function named append_sum that has one parameter named lst.s
# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

def last_two_added(lst):
  return lst[-1] + lst[-2]

def append_sum(lst):
  lst.append(last_two_added(lst))
  lst.append(last_two_added(lst))
  lst.append(last_two_added(lst))
  return lst


# test the function
print(append_sum([2, 4, 5])) # output will be [2, 4, 5, 9, 14, 23]


# 7.
# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst1) < len(lst2):
    return lst2[-1]
  elif len(lst1) == len(lst2):
    return lst1[-1]

# test the function
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10])) # output will be 5


# 8.
# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(lst1, lst2):
  combo_list = lst1 + lst2
  combo_list.sort()
  return combo_list

# test the function
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) # output will be [-10, 2, 2, 4, 5, 5, 10, 10]

# 9.
# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

def append_size(lst):
    size = len(lst)
    lst.append(size)
    return lst

# test the function
print(append_size([4, 3, 2, 1])) # output will be [4, 3, 2, 1 ,4]

# 10.
# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive).

def every_three_nums(start):
  lst = list(range(start, 100, 3))
  if start > 100:
    lst = []
    return lst
  else:
    return lst + [100]

# test the function
print(every_three_nums(50)) # output will be [50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 100]
