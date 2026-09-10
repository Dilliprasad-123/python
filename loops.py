# Looping Statements in Python

# Python provides two primary types of loops: `for` loops and `while` loops. These loops allow you to execute a block of code multiple times based on certain conditions.

# i = 1
# while i < 6:
#   print(i)
#   i += 1


'''
1
2
3
4
5
'''

#   using break statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

"""
  1
  2
  3
 """

#  using continue statement
# i=1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


'''
2
4
5
6

'''

# using else statement with while loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")