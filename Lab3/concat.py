#q12. Write a python program to enter two character array and print them combined
str1=input("Enter String 1")
str2=input("Enter String 2")
str3=""
a=0
b=0
for i in range(0,len(str1)+len(str2)):
    if(i%2==0):
        str3+=str1[a]
        a+=1
    else:
        str3+=str2[b]
        b+=1
print(str3)