#q13. Write a python program which takes strings as input and print all subset of it
str=input("Enter String")
for i in range (0,len(str)):
    for j in range(0,len(str)):
        print(str[i:j+1])