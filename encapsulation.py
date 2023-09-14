"""                               " encapsulation  "  -wrapping of data 

                                 scope :
                                        ->two access specifire
                                          1. public (default method )
                                          2. private
      """


class encap:
    a ='public'
    def deff(self):
        print("welcome to encapsultion")
obj = encap()
print(obj.a)
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