str = input("enter the string or character array ")
word = str.split(" ")
first = []
second = []
for i in range(0,len(word),2):
    first.append(word[i])
for i in range(1,len(word),2):
    second.append(word[i])
print(first)
print(second)