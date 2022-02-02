#q14. Write a python program to create a file, write multiple types of data in it and print the content
file=open("myfile.txt","w")
file.write("\nHello myname is Bighnesh Kumar Pati \n mY roll no is 1905603\n and i'm a third years student")
file.close()
file=open("myfile.txt","r+")
print("Content of the file: ")
print(file.read())