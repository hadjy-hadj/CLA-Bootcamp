#creating the list 
list=[]
for i in range(1,300):
    if i%2==0:
        list.append(i) #adding to the list even numbers 
print("YOUR LIST: ")
print(list) #printing our list

a=0 
for i in list:#itirating through the list to get the length of the list first
    a+=1
print("\n the length of this list is: ",a)

print("\n the squared values of the list are: ")
for i in list:
    if (i**0.5).is_integer():#condition to get squared values 
        print( i,end=" ")

print("\n",57 in list)#cheking if 57 is in our list 
