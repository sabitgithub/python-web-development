"""
while loop
___________

init variable
    while <condition>:
            statements
            .........

"""
start=int(input("Enter start value :"))
stop=int(input("Enter stop value :"))
i=start
while i<=stop:
    if i%2!=0:
        print(i,end="\t")
        # i=i+1
    i+=1 #compound assigned operator
    