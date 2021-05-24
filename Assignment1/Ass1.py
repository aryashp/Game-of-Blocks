import hashlib
import time
 
string1 = input("Enter the string: ")
ogstring = string1
flag = 0
i = 1
start_time = time.time()
while flag==0:
  bytes = ogstring.encode(encoding='UTF-8',errors='strict') # read entire file as bytes
  readable_hash = hashlib.sha256(bytes).hexdigest();
  if readable_hash[0]=='0' and readable_hash[1]=='0' and readable_hash[2]=='0' and readable_hash[3]=='0' and readable_hash[4]=='0':
    print("The hash value is:",readable_hash)  
    print("The nonce Value is:",i-1)
    flag=1
  ogstring = string1 + str(i)
  i+=1  
print("Time taken: %s seconds" % (time.time() - start_time))
