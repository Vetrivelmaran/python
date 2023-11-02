

#  ==================== EXCEPTION ERROR HANDLING ======================


# -----------------------1. SyntaxError ----------------------->

# try:
#     code="for i in range(10) print(i)"
#     exec(code)
# except SyntaxError:
#     print('syntax error')



# -----------------------2.indendation Error-------------------->

# if True:
# print('this makes indedation error')

# -----------------------3.Name Error -------------------------->


# print(s) 

# -----------------------4.Index Error------------------------->


# try:
#     a=[1,2,3]
#     print('this the second elemnt in a=%d'% a[1])
#     print('this is the last value in a=%d'% a[4])
# except IndexError:
#     print(' the index error acuure')
    
    

# -----------------------5.key error--------------------------->

# MySkill ={"programing":'python','frame work':'angular',1:True,0:False}

# try:
#     print(MySkill['1'])
# except KeyError:
#     print('key error ')

#------------------------6.file not found   Error--------------------------->


# try:
#     with open('hi.py','r') as file:
#         myfile=file.read()
# except FileNotFoundError:
#     print('file not found error')

# -----------------------7.zero divition error ----------------->

# def val(a:int):
#     result=10/a
#     print(result)
# try:
#     val(2)
#     val(0)
# except ZeroDivisionError as e:
#     print('zero divition error')

# ----------------------8.attribute error ----------------------->

# s='this code represent atrubute error'
# try:
#     s.appen('hello')
# except AttributeError:
#     print('attribute error')

# ----------------------9.type error----------------------------->
try:
    print('23'/2)
except TypeError:
    print('type error')