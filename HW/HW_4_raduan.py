################################################################################
#
# Raduan van Velthem Meira
# Python summer course 2022 -- Homework 4
# August 22, 2022
#
################################################################################

# Libraries and imports 

import random as rd
from datetime import datetime
import matplotlib.pyplot as plt
import math
import numpy as np
import array

# I got my algorithms from `https://realpython.com/sorting-algorithms-python/`

ordered_list = list(range(1,51))

random_list = ordered_list

rd.shuffle(random_list)

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array
  
def merge_sort(array):
  # If I can split the array
  if len(array) < 2:
    return array
  
  middle = len(array)//2
  
  return merge(
  left=merge_sort(array[:middle]),
  right=merge_sort(array[middle:]))
  

def merge(left, right):
  
  result = []
  index_left = index_right = 0
  
  while len(result) < len(left) + len(right):
  
    if left[index_left] <= right[index_right]:
      result.append(left[index_left])
      index_left += 1
    else:
      result.append(right[index_right])
      index_right += 1

    if index_right == len(right):
      result += left[index_left:]
      break

    if index_left == len(left):
      result += right[index_right:]
      break

  return result
  

# test  

random_list = ordered_list

rd.shuffle(random_list)

assert insertion_sort(random_list) == quicksort(random_list) == ordered_list

# No error indicating that the algorithm are sorting properly

# plot

random_list = []
time_first = []

for i in range(0,11):
  random_list = list(range(1,50*2**i))
  rd.shuffle(random_list)
  start_time = datetime.now()
  insertion_sort(random_list)
  end_time = datetime.now()-start_time
  time_first.append(end_time.seconds*1000 + end_time.microseconds/1000) # time in milliseconds


random_list = []
time_second = []

for i in range(0,11):
  random_list = list(range(1,50*2**i))
  rd.shuffle(random_list)
  start_time = datetime.now()
  merge_sort(random_list)
  end_time = datetime.now()-start_time
  time_second.append(end_time.seconds*1000 + end_time.microseconds/1000) # time in milliseconds

x_axis = []

for i in range(0,11):
  x_axis.append(50*2**i)



plt.subplots_adjust(left = .2, right = .95, top = .85, bottom = .3)

plt.plot(x_axis, time_first)
plt.plot(x_axis, time_second)


# Add a legend
plt.legend(['insertion sort', 'merge sort'], loc = "upper left", prop = {"size":10})


# y label
plt.ylabel("Time (in milliseconds)")
# x label
plt.xlabel("List size")
# plot title
plt.title("The Effect of Different Sort Algorithms on Runtime")

# Save plot
plt.savefig('C:\\Users\\radua\\onedrive\\washu\\classes\\python_course\\plot.pdf')

