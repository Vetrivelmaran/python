"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new ={}
for i in range(len(keys)):
   new.update({keys[i]:values[i]})
print(new,end="")
               #or

new =dict(zip(keys,values))
print(new)

"""
#---------------------------------------------------------------------------
"""        add two dict

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
"""

               #or
"""dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
new={**dict1,**dict2}
print(new,end="")
#-----------------------------------------------------------------------------
                    -------> find the history mark
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
x =sampleDict['class']['student']['marks']['history']
print(x)"""
#------------------------------------------------------------------------------
"""employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new={}.fromkeys(employees,defaults)
print(new)
------------------------------------------------------------------------------"""
"""sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

print(min(sample_dict))
print(sample_dict.get('Math'))
-------------------------------------------------------------------------------"""

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}	
}
sample_dict['emp3']['salary']=8500
print(sample_dict,)



