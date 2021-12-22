"""
tuple

"""

myTuple=(1,2,3,)
print(myTuple)

myTuple1=(1,"Hello",3.4,)
print(myTuple1)

myTuple2=("mouse",[8,4,6],(1,2,3,))
print(myTuple2)

myTuple3="Hello",
print(type(myTuple3))
print(myTuple2[1][2])
print(myTuple2[2][2])

myTuple5=("a","b","c","d","e","r","q","t","r","d")
print(myTuple5[-1])
print(myTuple5[0:3])
print(myTuple5[:3])
print(myTuple5[4:])

print(myTuple5.count('d'))
print(myTuple5.index('d'))

# TypeError: 'tuple' object doesn't support item deletion
# del myTuple5[1]
# print(myTuple5)

# print(dir(myTuple5))

print(len(myTuple5))