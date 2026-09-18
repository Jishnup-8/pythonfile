# Syntax ..

# 1 ) File = open ('file_name'  , 'mode')

# 2) with open ('file_name' , 'mode')as file:

# create file 

# with open('index.html' , 'x') as file:
#     print('file created')

# write ..
# with open('index.txt' , 'w') as file :
#     file.write('john\n i am from kannur \n welcome')

# # read ..
# with open ('index.txt','r') as file:
#     data = file.read()
#     print(data)

# read one line 

# with open('index.txt' , 'r') as file :
#     data = file.readline()
#     print(data)

# read all lines return an array 

# with open('index.txt','r') as file :
#     data = file.readlines()
#     print(data)

# update (append new data)

# with open('index.txt' , 'a') as file :
#     file.write('\nriya \nfrom calicut \nwelcome')

# modify existing data ..

# with open('index.txt' , 'r') as file :
#     data= file.read()

# update_data = data.replace('john' , 'jishnu')

# with open('index.txt', 'w') as file :
#     file.write(update_data)

#delete file 
# import os 
# os.remove('index.html')
