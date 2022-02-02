a,b = [int(x) for x in input("enter no and power ").split()]
temp = 1
for i in range(b):
    temp *= a
print("The output is",temp)