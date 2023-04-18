#FILES
file= open("numbers.txt",'r')

lines= file.readlines()
FileToWrite=open("evens.txt",'w')
for i in lines:
    if int(i)%2==0:
         FileToWrite.write(i.strip())
         FileToWrite.write("\n")
#CONTEXT MANAGERS

with open("numbers.txt",'r') as file:
     print(file.readlines())


