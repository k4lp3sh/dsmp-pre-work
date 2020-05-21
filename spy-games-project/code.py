# --------------
file_path

def read_file(path) :
    file = open(file_path)
    sentence = file.readline()
    file = file.close()
    return sentence

sample_message = read_file(file_path)
print(sample_message)



# --------------
#Code starts here
def fuse_msg(message_a,message_b):
    
    quotient=(int(message_b)//int(message_a))

    return str(quotient)


message_1=read_file(file_path_1)
print(message_1)

message_2=read_file(file_path_2)
print(message_2)


secret_msg_1=fuse_msg(message_1,message_2)


print(secret_msg_1)

#Code ends here


# --------------
#Code starts here

###############
def substitute_msg(message_c) :
    sub = ""
    if message_c == 'Red' :
        sub = 'Army General'
    elif message_c == 'Green' :
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
     
    return sub

message_3 = read_file(file_path_3)

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def compare_msg(message_d,message_e) :
    a_list = message_d.split()
    b_list = message_e.split()
    
    print(a_list)
    print(b_list)
    c_list = []
    [c_list.append(i) for i in a_list if i not in b_list]    
    return c_list

message_4 = read_file(file_path_4)
print(message_4)

message_5 = read_file(file_path_5)
print(message_5)

final_msg = compare_msg(message_4,message_5)
final_msg = list(final_msg)
print(final_msg)

secret_msg_3 = " ".join(final_msg)

print(str(secret_msg_3))




# --------------
#Code starts here

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word=lambda x: (len(x)%2==0)
    
    #Splitting the message into a list
    b_list=(filter(even_word, a_list))
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg

#Calling the function to read file
message_6=read_file(file_path_6)

#Calling the function 'filter_msg'
secret_msg_4=extract_msg(message_6)

#Printing the secret message
print(secret_msg_4)

#Code ends here


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
print(message_parts)

final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)
print(secret_msg)

def write_file(secret_msg,path) :
    f = open(path,'a+')
    f.write(secret_msg)
    f.close()

write_file(secret_msg,final_path)
print(secret_msg)


