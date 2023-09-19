"""                               " encapsulation  "  -wrapping of data 

                                 scope :
                                        ->two access specifire
                                          1. public (default method )
                                          2. private
      """


class encap:
    __a ='public'
    def deff(self):
        print("welcome to encapsultion")
obj = encap()
print(obj._encap__a)
obj.deff()

"""
                                             it is code for private scope. here we get error because 
                                             it is private scop ( __prefix of  variable ) 
                                             otherwise we can't access the  variables and function(methodds)
                                             outside the class
class encap:
    a ='public'
    def deff(self):
        print("welcome to encapsultion")
obj = encap()
print(obj.a)
obj.deff()

"""



"""class Encap:
    __a = 'public'
    
    def deff(self):
        print("Welcome to encapsulation")

obj = Encap()
print(obj._Encap__a)  # Access the '__a' attribute using name mangling
obj.deff()
In the code above, we use obj._Encap__a to access the __a attribute. 
However, please note that name mangling is a way to indicate that an attribute 
should be treated as private, but it's still technically accessible if you know the mangled name.
It's not as strict as some other languages' encapsulation mechanisms."""