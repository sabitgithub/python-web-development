def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

# value=factorial(5)
# print(value)         


def fabonacci(n):
        if n ==0:
            return [0]
        elif n ==1:
             return [0,1]
        else:
            fibo=fabonacci(n-1)
            nextElement=fibo[n-1]+fibo[n-2]
            fibo.append(nextElement)
            return fibo

# val=fabonacci(0)
# print(val)

def check_prime(n,i=2):
     if n==i:
         return True
     else:
        if n%i==0:
             return False
        else:
              return check_prime(n,i+1)


print(check_prime(16))



