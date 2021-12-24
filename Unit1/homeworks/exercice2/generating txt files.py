#PROGRAM THAT GENERATES 26 txt FILES FROM A.txt TO Z.txt
from string import ascii_uppercase
file=ord("A")
list=[]
while file<=ord("Z"):
    name=chr(file)
    file+=1
    list.append(name)#craeting a list that contains all alphabts 

#using the previous list to generat files 
for name in list:
    with open(name+".txt","x") as f:
        f.writelines(name)
