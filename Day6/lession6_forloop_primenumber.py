def prime(x,y):
    for n in range(x,y):
        isPrime=True
        for i in range(2,n):
            if n%i==0:
                isPrime=False
                break
            
        if isPrime:
            print(n,end="\t")

prime(1,10)
print("_"*80)
prime(100,120)
print("_"*80)
prime(127,234)
    