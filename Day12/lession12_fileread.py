file=open('text.txt','r')
# data=file.readlines()
# for x in data:
#     print(x)

# print(file.read()) #Read entier file

# print(file.read(12))

# print(file.readline()) # To Read single line

sl=1
for n in file:
    print(sl,'-',n)
    sl=sl+1

file.close
