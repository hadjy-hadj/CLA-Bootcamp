# READ THE N FIRST LINES OF THE FILE 
n=int(input("give us the number of lines you want to extract from this file: "))
print("your ",n," first lines of the files are: ")
with open("./student_names.txt") as file:
    for lines in (file.readlines()[:n]):
        print(lines)


# READ THE LAST N LINES OF THE FILE 
n=int(input("give us the number of lines you want to ectract from this file: "))
print("your ",n," last lines of the files are: ")
with open("./student_names.txt") as file:
    for line in (file.readlines()[-(n+1):]):
        print(line)


#CHECK IF A NAME IS IN THE FILE
name=input("enter the name you want to check: ")
print( name in open("./student_names.txt") ) 
