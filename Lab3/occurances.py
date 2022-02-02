#q8.Write a python program to find an occurence of a particular character in a string
str=input("Enter string")
ch=(input("enter character"))
c=0
for i in range(0,len(str)):
    if(ch==str[i]):
        c+=1
print("Total occurence =",c)