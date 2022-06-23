# Write a Python function called max_num() to find the maximum of three numbers.

from math import factorial
from random import triangular
import re


def max_num(x,y,z):
    return max ([x,y,z])

print(max_num(1,2,3))
print(max_num(30, 50, 60))
print(max_num(100,200,300))

# Write a python function called multi_list() to multiply all the numbers in a list

def mult_list(lst):
    if len(lst) == 0:
        return 0

        factorial = lst[0]

        if len(lst) > 1:
            for i in lst[1:]:
                factorial = factorial * i
            
            return factorial

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

# Write a python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::-1]

print(rev_string(""))
print(rev_string("sandwich"))
print(rev_string("meat"))

#Wrtie a python function called num_within() to check whether a number falls in a given range

def num_within(x,y,z):
    return x in range(y,z+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  # your code here
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2

    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        
        if i == 0:
          row.append(1)
        
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)