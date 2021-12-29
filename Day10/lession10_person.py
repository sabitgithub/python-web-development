class Person:
    def __init__(self,n,a) -> None:
        print('I am from person class')
        """
        init as constructor
        """


        self.name=n
        self.age=a

    def show(self):
        print(f"I'm {self.name} and {self.age} yrs old")

    def setName(self,para_name):
         self.name= para_name     
    def setAge(self,para_age):
         self.age= para_age

    def getName(self):
         return self.name
    def getAge(self):
         return self.age              



# p1=Person('Salam','23')
# p1.show()
# p2=Person('Ayman','16')
# p2.show()

# print(p1.getName())
# print(p2.getAge())
# # p1.setName('Waliur Rahman')
# # p1.setAge('24')

# print(f"Hello!! Mr {p1.getName()} . Are you {p1.getAge()} yrs old??")


"""
inheritance
syntex

class BaseClass():
    body of baseclass

class DerivedClass (BassClass):
    body of DerivedClass    
"""

class Students(Person):
    def __init__(self, n, a, f) -> None:
        super().__init__(n, a)
        print("I'm from Students Class")
        self.fess=f
    
    #Overriding 

    def show(self):
        print(f"Name : {self.name}\nAge : {self.age}\nFees : {self.fess}")

    def setFees(self,para_fees):
        self.fess=para_fees    



std1=Students('Sabit',20,50)
std1.setName('Anzam')
std1.setAge('25')
std1.setFees('2500')
std1.show()



