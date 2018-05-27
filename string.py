str1 = "I am String in Python"
str2 = 'I am also a String in Python'

length = len(str1) # returns the length of the string;
print(length)

print(str1[0])
print(str1[-1])

print(str1[1:5]) # starting from position 1 to 5
print(str1[:5]) # starting from position 0 to 5
print(str1[5:]) # starting from position 5 to last

str3 = 'Con' + 'catination'
print(str3)

word = "Ford"
word = "L" + word[1:]
print(word)




# String format method:
# Using position:
print("Today I {0} for {1} hours".format("slept", 10))

# Using variables:
print("Prices: ({x}, {y}, {z})".format(x = 1, y = 2, z = 3))

# Using Multiple
print("The {vehicle} had {0} crashes in {1} months".format(5, 6, vehicle = "Car"))

# String left alingment with custom positions
print("{:<20}".format("test"))

# String right alingment with custom positions
print("{:>20}".format("test"))

print("{:b}".format(21)) # returns the binary value of 21

print("{:x}".format(21)) # returns the hexadecimal value of 21

print("{:o}".format(21)) # returns the octal value of 21

print("""\
    Hello:
        User Defined look
            Pytho Outputs """) # removes the space in starting
print("""
    Hello:
        User Defined look
            Pytho Outputs """) # gives the space in starting