# --------------
##File path for the file 
path=file_path
def read_file(path):
    file=open(path,mode='r')
    sentence=file.readline()
    file.close()
    return sentence
sample_message=read_file(path)
    



#Code starts here


# --------------
#Code starts here
def fuse_msg(message_a,message_b):
    quotient=(int(message_b)//int(message_a))
    return str(quotient)
path1=file_path_1
path2=file_path_2
message_1=read_file(path1)
message_2=read_file(path2)
print(message_1)
print(message_2) 
secret_msg_1=fuse_msg(message_1,message_2)





    








# --------------
#Code starts here
def substitute_msg(message_c):
    if(message_c=='Red'): 
        sub='Army General' 
    elif(message_c=='Green'): 
        sub='Data Scientist' 
    else:
        sub='Marin Biologist'
    return sub;  
path_3=file_path_3
message_3=read_file(path_3)
print(message_3)
secret_msg_2=substitute_msg(message_3)    



# --------------
# File path for message 4  and message 5

#Code starts here
def compare_msg(message_d,message_e):
    a_list=[message_d.split()]
    b_list=[message_e.split()] 
    c_list=['you','are','now']
    final_msg=" ".join(c_list)
    return final_msg
path_4=file_path_4
path_5=file_path_5
message_4=read_file(path_4)
message_5=read_file(path_5)
print(message_4)
print(message_5)
secret_msg_3=compare_msg(message_4,message_5)











# --------------
#Code starts here
def extract_msg(message_f):
    a_list=[message_f.split()]
    even_word=lambda x:len(x)%2==0
    b_list=list(filter(even_word,a_list))
    b_list=['step','closer','to','become']
    final_msg=" ".join(b_list)
    return final_msg
path_6=file_path_6
message_6=read_file(path_6)
print(message_6)
secret_msg_4=extract_msg(message_6)




# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

def write_file(secret_msg,path):
    file=open(final_path,mode='a+')
    file.write(secret_msg)
    file.close()
message_parts=[secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
secret_msg=" ".join(message_parts)    
write_file(secret_msg,final_path) 
print(secret_msg)   
    
    



