import uuid
import random
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols =['!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '+', '=', '?']
password=""
numbers=0
idv1 = str(uuid.uuid1())
idv4 = str(uuid.uuid4())
for i in range(0, len(idv4)-1, 3):
    if not(idv4[i].isdigit() or idv4[i] == "-"):
        password += idv4[i]
        numbers += 1
        if(numbers == 4):
            break
        
for i in range(0, len(idv1)-1, 3):
    if(idv1[i].isdigit()):
        password += idv1[i]
        numbers += 1
        if(numbers == 8):
            break
        
for i in range(0, len(idv1)-1):
    if(idv1[i].isdigit() and idv1[i+1].isdigit()):
        password += alphabets[int(idv1[i]+idv1[i+1])%26]
        numbers += 1
        if(numbers == 12):
            break
        
for i in range(0, len(idv1)-1):
    if(idv4[i].isdigit() and idv4[i+1].isdigit()):
        password += symbols[int(idv4[i]+idv4[i+1])%14]
        numbers += 1
        if(numbers == 16):
            break         
  
print(idv1, idv4)
pwd = ''.join(random.sample(password, 16))
print(pwd)

