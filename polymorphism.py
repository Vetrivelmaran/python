
"""
                                        polymorphism
                                        ------------

                #ploymorphism allows us to perfome a single action in different ways

                #    --- 1.Runtime poluymorphisam
                #   |    2.compile time poliymorphisam --
                    |                                   |
                    |                                   | 
                    |          *method  overloading------
                    |--------->*method  overwritie
                               *operator overloading
"""

                                    # method overloading
"""class new:                  
        def fun(self,a=None,b=None,c=None):
            if a!=None and b!=None and c!=None:
                return a+b+c
            elif a!=None and b!=None:
                return a+b
            else:
            
                return a
ob = new()
print(ob.fun(10,70,40))
"""

"""class new1:
    def over(self,*any):
        som =0
        for  i in any:
            som+=i
        print(som)
obj = new1()
obj.over(10,20,30,40)"""


#                                  method overrinding
"""class mugil:
    def project(self):
        print("confrence management system \n")

class rep(mugil):
    def project(self):
        super().project()
        print("online video maker\n")
class vetri(rep):
    def project(self):
        super().project()
        print('secure data backup system\n')
        



ob =vetri()
ob.project()"""
#                                  operator overloding

                    # operator overloding used to perfome the +,-,*,/ between two objects
# class project:
#     def __init__(self,a) -> None:
#         self.a=a
       
#     def __add__(self,other):
#         return self.a+other.a
#     def __mul__(self,new):
#         return self.a*new.a            

# obj1 = project(10)
# obj2 = project(20)
# print('sum value:',obj1+obj2)   #---> here we add two abjects
# print('sum value:',obj1*obj2)

