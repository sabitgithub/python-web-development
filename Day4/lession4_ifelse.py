#User Login

u=input('Enter your user name: ')
p=input('Enter your password: ')

if u.upper() =='Admin'.upper() and p=='123':
    print(f"Welcome Mr {u}")
elif u.upper !='Admin'.upper() and p=='123':
    print("Invalid username")    
elif u.upper =='Admin'.upper() and p!='123':
    print("Invalid password")
else:
    print("Username & Password both invalid")        