"""
dictonary
variable = {'key':'value'}
"""

data={'id':'1','name':'Sabit','age':'20'}

print(data)
print(data['name'])
print(data['age'])

# modify data using key

data.update({'age':'18'})
print(data)

data.update({'marks':'90'})
print(data)

del data['name']
print(data)

print(dir(data))

# display items

print(data.items())
print(list(data.items()))
print(list(data.keys()))

for n in data.keys():
        print(n)
for n in data.values():
        print(n)

for x,y in data.items():
        print(f"{x}={y}")

list_data=list(data.items())
list_data.sort()
# list_data.sort(reverse=False)
print(list_data)


employees={}
employees['id']='1'
employees['name']='1'
employees['age']='20'
employees['address']='Nikunja-2'
employees['dept']='IT'
employees['phone']='01745871019'

print(employees)
print(employees['address'])
print(employees.get('address'))
print(sorted(employees)) 
# temporary sorted.

"""
distonary comprehension
"""

squares={x:x*x for x in range(6)}

print(squares)
print(len(squares))
# print(help(squares))
# print(help(squares.pop()))

print(squares.pop(3))
# print(squares.pop(6,"Not Found"))
# print(squares.pop(6,"Not Found"))
# print(squares)

squares=[x*x for x in range(6)]
# print(squares)

students=[
    {'id':'1','name':'sabit','age':'20'}, 
    {'id':'2','name':'abc','age':'30'},
    {'id':'3','name':'xyz','age':'40'},
    {'id':'4','name':'qqq','age':'50'}
]

import os
os.system('cls')
print("%-5s %-20s %-10s"%(['id'],['age'],['name']))
print("_"*80)
for std in students:
    print("%-5s %-25s %-10s"%(std['id'],std['age'],std['name']))