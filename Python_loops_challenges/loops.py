# 1.
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count


# test the function
print(divisible_by_ten([20, 25, 30, 35, 40, 50, 100])) # output will be 5


# 2.
# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

def add_greetings(names):
  lst = []
  for name in names:
    lst.append("Hello, " + name)
  return lst

# test the function
print(add_greetings(["BlahBlah", "Sunshine", "Gorgie"])) # output will be ['Hello, BlahBlah', 'Hello, Sunshine', 'Hello, Gorgie']


# 3.
# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst.pop(0)
  return lst


# test the function
print(delete_starting_evens([4, 6, 8, 11, 12, 15])) # output will be [11, 12, 15]
print(delete_starting_evens([4, 6, 8])) # output will be []


# 4.
# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    if index % 2 != 0:
      new_lst.append(lst[index])
  return new_lst

# test the function
print(odd_indices([4, 3, 7, 10, 11, -2])) # output will be [3, 10, -2]


# 5.
# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_index = base ** power
      new_lst.append(new_index)
  return new_lst


# test the function
print(exponents([2, 3, 4], [1, 2, 3])) # output will be [2, 4, 8, 3, 9, 27, 4, 16, 64]


# 6.
# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
  if sum(lst1, 0) > sum(lst2, 0):
    return lst1
  elif sum(lst1, 0) < sum(lst2, 0):
    return lst2
  elif sum(lst1, 0) == sum(lst2, 0):
    return lst1

# test the function
print(larger_sum([1, 9, 5], [2, 3, 7])) # output will be [1, 9, 5]


# 7.
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

def over_nine_thousand(lst):
  lst_sum = 0
  while True:
    for i in lst:
      lst_sum = lst_sum + i
      if lst_sum > 9000:
        break
    return lst_sum

# test the function
print(over_nine_thousand([8000, 900, 120, 5000])) # output will be 9020


# 8.
# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

def max_num(nums):
  return max(nums)

# test the function
print(max_num([50, -10, 0, 75, 20])) # output will be 75

# 9.
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.

def same_values(lst1, lst2):
  new_list = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_list.append(index)
  return new_list

# test the function
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])) # output will be [0, 2, 3]


# 10.
# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

def reversed_list(lst1, lst2):
  lst2.reverse() # reverses the list but retruns none becuase it doesn't take on the value
  if lst1 == lst2:
    return True
  else:
    return False

# test the function
print(reversed_list([1, 2, 3], [3, 2, 1])) # output True
print(reversed_list([1, 5, 3], [3, 2, 1])) # output False
