"""
while True:
    msg=input("Enter a message :")
    if msg=="x":
        break 
    print(msg)
    
"""

# i=1
# sum=0
# while i<=10:
#     if i==10:
#         print(i,end="")
#     else:
#         print(i,end="+")
#     sum+=i
#     i+=1
# print("=",sum)     

# i=1
# sum=0
# while i<=10:
#     print(i,end="+")
#     sum+=i
#     i+=1
# print("\b=",sum)


# Fibonacci Series

# a,b=0,1

# while b<10:
#     print(b,end="\t")
#     a,b=b,b+a

# Factorial
"""
4!=4X3X2X1 =24

"""

n=int(input("Enter to the value of n :"))
f=1
i=1

while i<=n:
    f*=i
    i+=1
print(f'The facotial of {n} is {f}')
