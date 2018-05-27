greet = "hello"

if greet == "hello" or greet == "hi":
    print("Hi, How r u")

# --------------------------------------------

greet = ""

if greet == "hello" or greet == "hi":
    print("Hi, How r u")
else:
    print("Hey!")

# --------------------------------------------

if 5 < 7:
    if 5 > 6:
        print("5 > 6")
    else:
        print("5 < 6")
else:
    print("not true")

# --------------------------------------------

greet = "hello"

if greet == "hi":
    print("hello!")
elif greet == "hello":
    print("Hi, How r u!")
else:
    print("Hey!")
# --------------------------------------------

# ternary (conditional) operator
greet = "hello"
voice = "Hi" if greet == "Hello" or greet == "Hi" else "Hey"
print(voice)
