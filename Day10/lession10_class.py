"""
1. Class is blue print for the object
2. An object has two characteristics
3. i) Attribute
   ii) behaviour

syntex

class <ClassName> (objet)
        <snippets>

making an instance (object) from a class.
objectName = ClassName(arguments)
"""

class MyClass (object):
    """
   This is sample class
    """
    a=10

    def myfunc(self):
        print('hello')


"""
creating an object
"""        

obj1=MyClass()
print(obj1.a)
obj1.myfunc()
print(MyClass.__doc__)