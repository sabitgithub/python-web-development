"""
File
__________
the syntex to open a file object in Python

Syntex:
file_object=open("filename","mode")

modes are :
1. 'r'  - read mode (default)
1. 'w'  - write mode ()
1. 'a'  - append mode ()
1. 'r+'  - special read & write mode ()
"""

# file=open('text.txt','w')
# file.write('Hello World\n')
# file.write('This is our new test file\n')
# file.write('and this is another file\n')
# file.close

file=open('text.txt','a')
file.write('This is from Append mode\n')
file.write('This is append testing\n')
file.close


