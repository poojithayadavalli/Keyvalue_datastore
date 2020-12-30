import time

d={}
#'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can proceed by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in d:
        print("Error: this key already exists") #error
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Json object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                else:
                    print("Error: Key length should not exceed 32characters")#error
            else:
                print("Error: Memory limit exceeded!! ")#error
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("Error: key does not exist in datastore. Please enter a valid key") #error
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JsonObject i.e.,"key_name:value"
                return stri
            else:
                print("Error: time-to-live of",key,"has expired") #error
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("Error: key does not exist in datastore. Please enter a valid key") #error
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error
        else:
            del d[key]
            print("key is successfully deleted")


