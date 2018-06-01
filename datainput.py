# Data Input

age = input("How old are you: ")
print(age)

# File Management:
# open(filepath, access, buffering)

file = open("files/read.txt", "r")
print(file.read())  # reads the file
print(file.read(7))  # reads the specific length of charecters
file.seek(15) # moves the position of the cursor in the file
print(file.tell())  # tells the position of the cursor in the file
file.close()  # closes the file

for line in file:  # to print the content line by line inside the file
    print(line)

file.close()

print("File Name: " + file.name) # returns name of the file includes path
print("Is Closed: " + str(file.closed)) # returns the bool value wheather the file is closed or not
print("Mode: " + file.mode) # returnd the mode of the file read or write


file = open("files/write.txt", "w+") # w+ used for read and write
file.write("Hi, hello I'm a string")
file.seek(0)
print(file.read())
file.close()