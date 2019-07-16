# Hello World program in Python
    
import re

sessame = "[\w]+\.[\w]+"

ss = re.search(sessame, "sathish-ext.prakashe3")


if ss:
    print("Sessame Matches")
else:
    print("Sessame Not Matching")
  

email = "sathish.prakash@socgen-ext.coms"
em = re.search("^[\w\.\+\-]+\@[\w-]+\.[a-z]{2,3}$", email)


if em:
    print("Email Matches")
else:
    print("Email Not Matching")
    
    
input = "sathishkr.~cs@gmail.com"

m = re.search('[^@]+@[^@]+\.[^@]+',input)

if m:
    print("Email String found.")
else:
    print("Email Nothing found.")
  
