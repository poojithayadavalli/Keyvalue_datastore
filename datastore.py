import time

dic={}
#'dic' is the dictionary in which we store data

#for create operation 
#syntax "create(key_name,value,timeout_value)" timeout is optional you can proceed by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dic:
        print("Error: this key already exists") #error
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Json object value less than 16KB 
                if timeout==0:
                    val=[value,timeout]
                else:
                    val=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=val
                else:
                    print("Error: Key length should not exceed 32characters")#error
            else:
                print("Error: Memory limit exceeded!! ")#error
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
# syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("Error: key does not exist in datastore. Please enter a valid key") #error
    else:
        temp=dic[key]
        if temp[1]!=0:
            if time.time()<temp[1]: #comparing the present time with expiry time
                st=str(key)+":"+str(temp[0]) #to return the value in the format of JsonObject i.e.,"key_name:value"
                return st
            else:
                #print(time.time(),temp[1])
                print("Error: time-to-live of",key,"has expired")#error
                del dic[key]
        else:
            st=str(key)+":"+str(temp[0])
            return st

#for delete operation
#syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("Error: key does not exist in datastore. Please enter a valid key") #error
    else:
        b=dic[key]
        if temp[1]!=0:
            if time.time()<temp[1]: #comparing the current time with expiry time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error
        else:
            del d[key]
            print("key is successfully deleted")


