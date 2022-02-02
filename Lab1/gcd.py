def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = int(input("Enter the first Number"))
b = int(input("Enter the second Number"))

print("The gcd of {0} and {1} is :".format(a,b),hcf(a,b))