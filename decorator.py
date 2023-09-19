"""  DECORATOR - decorator allow to change fucntions functionality withoud change the source coad diractly 
    -----------
1) FUNCTION DECORATOR
2) CLASS DECORATOR


1) single decorator
2)multiple decorator


1)with argument
2)without argument
"""

# def upperstring(ref):
#     def Process():
#         data=ref()
#         return data.upper()
#     return Process
# @upperstring
# def MyFunction():
#     return "welcome to the decorator"

# print(MyFunction())
# result = upperstring(MyFunction)
# print(result())
import pickle
a=[1,2,3,5]
dump=pickle.dumps(a)
b=pickle.loads(dump)
print(a==b)
