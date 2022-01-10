import os



try:
    os.mkdir("tempdir")
    
except Exception as ex:
    print('File Already exists!! ',ex.args[1])    
# os.chdir("tempdir")
print(os.getcwdb())

# os.rmdir('tempdir')
print(os.getcwdb())

if os.path.exists('text.txt'):
        os.remove('text.txt')
else:
    print('The file does not exists')