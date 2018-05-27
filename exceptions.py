try:
    a = 5/0
except Exception as e:
    print(e)

#-----------------------------------------

try:
    n = int(input("Enter an Integer: "))
except ValueError:
    print("Value is not an Integer")

#-----------------------------------------

try:
    sum = 0
    file = open("num.txt", "r")
    for num in file:
        sum = sum + 1.0/int(num)
    print(sum)
except ZeroDivisionError:
    print("Number in file equals to Zero")
except IOError:
    print("File DNE")
finally:
    print(sum)

#-----------------------------------------

a = 1
def raisedException(a):
    if type(a) != type("a"):
        raise ValueError("a is not a type of String")

try:
    raisedException(a)
except ValueError as e:
    print(e)