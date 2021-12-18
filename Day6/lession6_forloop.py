"""
for loop
syntax:
for item in collection:
    statement
"""
'''
x=list(range(10,50,2))
print(x)'''


'''y=list(range(50,10,-1))
print(y)'''


'''for i in range(20):
    print(i,end="\t")
'''
# for i in range(20,50):
#     if i%2==1:
#         print(i, end="\t")
'''fruits=["apple", "banana", "orange", "mango"]
print(fruits[1])
for x in fruits :
    print(x)'''

'''n=4
f=1
for i in range (1,n+1):
    f=f*i
print("The factorial of "+str(n)+" is "+ str(f))'''
# a=0
'''for i in range (10+1):
    a+=i
print(a)'''

# for i in range(65,91):
#     print(chr(i),end="\t")
# for i in range(123,97):
#      print(chr(i),end="\t")

# letter= input("Enter the Letter to get the ascii value: ")
# print(ord(letter))

# import time
# for j in "i love python":
#     time.sleep(1)
#     print(j, end=" ",flush=True)


# n=int(input("Number: "))

# for i in range(2,n):
#     if n%i==0:
#         print("this number is not a prime number")
#         break
#     else:
#         print("This is a prime number.")
#         break


n=int(input("Number: "))
isPrime=True
for i in range(2,n):
    if n%i==0:
        isPrime=False
        break

if isPrime:
    print("This is a prime number")
else:
    print("This is not a prime number")