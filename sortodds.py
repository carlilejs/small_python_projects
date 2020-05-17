# Your task is to sort ascending odd numbers but even numbers must be on their places.
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

import Test

def sort_array(arr):
	# Sort an array of the odd numbers from original array
	# Use reverse so that pop() can be used below to pull smallest numbers off the end
  	odds = sorted([x for x in arr if x % 2 != 0], reverse = True)
  	# Create and return a new array with odd numbers replaced from the descending odds array
	return [x if x % 2 == 0 else odds.pop() for x in arr]

Test.assert_equals(sort_array([3,2,1,4,4,6,1,8]), [1,2,1,4,4,6,3,8])
# print(arr) # [3,2,1,4,4,6,1,8]
# print(sorted_odds) # [1,2,1,4,4,6,3,8]