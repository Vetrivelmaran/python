#                                                      Exercise 3-1.
# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is
# in column 70 of the display:

"""def right_justify(s):
    print(' '*(70-len(s))+s)
right_justify('vetri')"""


#                                                       Exercise 3-3.



# Note: This exercise should be done using only the statements and other features we
# have learned so far.
# 1. Write a function that draws a grid like the following:
# print('+','-'*4,'+','-'*4,'+')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('+','-'*4,'+','-'*4,'+')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('|'+('  '*3)+'|'+('  '*3)+'|')
# print('+','-'*4,'+','-'*4,'+')

# print('\n')
# def cell():
#     print('+','-'*4,'+')
#     print('|'+('  '*3)+'|')
#     print('|'+('  '*3)+'|')
#     print('|'+('  '*3)+'|')
#     print('|'+('  '*3)+'|')
#     print('+','-'*4,'+')
    # return 1
    

# def grid(row,column):
#     count=0
#     for i in range(row):
#         cell()
#         count+=1
#         if count==row:
#             for j in range(column):
#              cell()
    
# row=int(input('enetr the row:'))
# column =int(input('enter the column:'))
# grid(row,column)
    

# def grid():
#     for i in range(2):
#             print('+','-'*4,'+')
#             print('|'+('  '*3)+'|')
#             print('|'+('  '*3)+'|')
#             print('|'+('  '*3)+'|')
#             # print('|'+('  '*3)+'|')
#             # print('+','-'*4,'+')
#         # print(end='')
#     # for i in range(2):
#         # cell()
#         # print(end='')
# # grid()

        
# for i in range(11):
#     if i%5==0:
#       print('+','-'*4,'+','-'*4,'+')
#     else:                                                 ----------------> ok
#       print('|'+('  '*3)+'|'+('  '*3)+'|')

