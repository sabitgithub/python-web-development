"""
def function_name():
    doc string
    ...
"""

def welcome():
    print("Good morning!! Waliur Rahman Sabit")

# welcome()

def welcome1(name,msg):
    print(f"Good morning!!{name} {msg}")

# welcome1('Sabit','Welcome')    

def welcome3(name='Waliur Rahman',msg='Welcome Back'):
    print(name,msg)
# welcome3()
# welcome3('SABIT','Bye')

def welcome4(x,y,z):
    print(f"Hello {x}")
    print(f"Hello {y}")
    print(f"Hello {z}")

# welcome4('sabit','waliur','rahman')


"""
arbitrary arguments

"""

# def welcome5(*names):
#     for x in names:
#         print(f'Hello {x}')

# print(5*'_____')
# welcome5('Salam','Anzam','Sabit')   

# def double(x):
    # return x*2

# z=double(3)    
# print(z)    
# print(double(5))

# alternative way using lamda function:
# function_name = lamda arguments:expression

# double=lambda x: x*2
# print(double(10))

# def buildProfile(**user_info): #** dictonary
#     profile={}
#     for key,value in user_info.items():
#         profile[key]=value
#     return profile


# myProfile=buildProfile(name='Sabit',address='Nikunja-2',field='IT')
# print(myProfile)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mul(x,y):
    return x*y
def mod(x,y):
    return x%y

print(add(3,5))



