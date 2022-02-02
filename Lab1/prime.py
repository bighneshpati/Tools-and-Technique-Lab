a = int(input("Enter the number which has to be checked whether it is prime or not"))
count = 0
for i in range(2,a):
    if a % i == 0:
        count += 1
if count > 0:
    print("Not prime")
else:
    print("Prime")
