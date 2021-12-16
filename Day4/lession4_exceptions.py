#design menu

while True:
    print('Main Menu')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    print('Enter your selection: ', end= '')

    x=input()

    if x=='1':
        a=int(input('a : '))
        b=int(input('b : '))
        print('Addition is %s'%(a+b))
    elif x=='2':
        a=int(input('a : '))
        b=int(input('b : '))
        print('Subtraction is %s'%(a-b))
    elif x=='3':
        a=int(input('a : '))
        b=int(input('b : '))
        print('Multiplication is %s'%(a*b))
    elif x=='4':
        a=int(input('a : '))
        b=int(input('b : '))
        print('Division is %s'%(a/b))
    elif x=='5':
        print('Goodbye!!')
        break
    else:
        print('Invalid Selection')