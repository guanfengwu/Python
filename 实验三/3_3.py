
import sys
import string

password=input()

pwtype=password.isalnum()

int_count=0
for x in password:
    if x.isdigit():
        int_count+=1
    
if len(password)>=8:
    if pwtype:
        if int_count>=2:
            print("Valid password")
            sys.exit()
        
print("Invalid password")  
