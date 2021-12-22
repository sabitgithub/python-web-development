"""
list
______
variable=[]
"""

# motoCycles=['Yamaha','Suzuki']
# print(motoCycles)
# print(motoCycles[0])
# print(motoCycles[1])

# motoCycles.append('Hero')
# print(motoCycles)
# # motoCycles.append('Dukati')
# motoCycles.insert(1,'Dukati')

# for n in motoCycles:
#         print(n,end="\t")

# x=0
# while x<len(motoCycles):
#     print(motoCycles[x])
#     x=x+1 


# fruits=[]
# fruits.extend(['mango','banana','orange'])
# print(fruits)
# fruits.append('apple')
# fruits.insert(1,'grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
# fruits.pop(1)
# print(fruits)
# del fruits[2]
# print(fruits)
# fruits.remove('apple')
# print(fruits)

cars=['BMW','Audi','Corola','Subaro','Toyota','Honda','Audi']

# # print(f"Total number of cars {len(cars)}")
# cars.reverse()
# print(cars)
# print(cars.index('Honda'))
# print(cars[-1])
# print(cars[-3])
# print(cars[0:3])
# print(cars[2:5])
# print(cars[2:])

num=list(range(10))
print(num)
print(sum(num))
print(min(num))
print(max(num))
print(sum(num)/len(num))

print(cars.count('Audi'))
# print(dir(cars))
cars.clear()
print(cars)

# i=10
# print(dir(i))
# print(type(i))