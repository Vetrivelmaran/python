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
# for i in range(11):
#     if i%5==0:
#       print('+','-'*4,'+','-'*4,'+')
#     else:                                                 
#       print('|'+('  '*3)+'|'+('  '*3)+'|')
      
# Exercise 11-1.
# Write a function that reads the words in words.txt and stores them as keys in a dic‐
# tionary. It doesn’t matter what the values are. Then you can use the in operator as a
# fast way to check whether a string is in the dictionary.

# import pickle
# a={'v':1,'e':2,'t':3}
# with open('text.pkl','wb') as file:
#   pickle.dump(a,file)
# with open('text.pkl','rb') as file:
#   # print(pickle.load(file))
#   key=input('enter the key')
#   if key in pickle.load(file):
#     print('yes')
#   else:
#     print('key not found')


#---------------------------------------------------------function overloading
# class MyFunction:
#     def fun(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# ob=MyFunction()
# print(ob.fun(1))
# print(ob.fun(23,44))
# print(ob.fun(23))

#--------------------------------------------------------function overloading using varable length argument
# class Myfunc:
#     def fun(hi,*what_you_want):
#         sum=0
#         for i in what_you_want:
#             sum+=i
#         print('sum of valus:',sum)
# ob=Myfunc()
# ob.fun(12,32,34,45,23)
# ob.fun(32,34,45,23)
# ob.fun(34,45,23)
# ob.fun(12,32)

#-------------------------------------------------------function overriding
# class parent:
#     def fun(dfg):
#         print('parent class')
# class child(parent):
#     def fun(rf):
#         super().fun()
#         print('child')
# class grandchild(child):
#     def fun(self):
#         super().fun()
#         print('grand chile')
# ob=grandchild()
# ob.fun()
    

#--------------------------------------------------------operator overriding
# class employee:
#     def __init__(self,name,days) -> None:
#         self.day=days
#         self.name=name
#     def __mul__(self,other):
#         return self.day*other.salary
    
# class payroll:
#     def __init__(self,salary) -> None:
#         self.salary=salary
        

# ob1=employee('Ram',28)
# ob2=payroll(2000)
# print(f'total day {ob1.name} present officce {ob1.day}')
# print(f'{ob1.name} salary for this month {ob1*ob2}')

#----------------------------------------------------__getitem__


# class empl():
#     def __init__(self,val) -> None:
#         self.val=val
    
#     def __getitem__(self,index):
#         print(self.val[index])

#     def __setitem__(self,index,item):
#         self.val[index]=item
#         print(self.val)

# ob=empl([23,'vetri',300000])
# print(ob.val[2]) 
# ob.val[1]=233434
# print(ob.val)
# Example: Creating a simple function decorator
# Example: Unpacking values from an iterable    