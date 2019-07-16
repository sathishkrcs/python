import re

try:
    print(x)
except:
    print('Error')

try:
    fh = open("test.txt", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")

pt = "[a-b]+\.[a-b]+"

pr = re.search(pt, 'sathish.prakash')

print(pr)

if (pr):
    print('success')
else:
    print('No Match')
