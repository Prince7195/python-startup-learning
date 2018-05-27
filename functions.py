def fn():
    print("I'm Function")

fn()

#-------------------------------------------

def returnFn():
    return "I'm Returning Function"

result = returnFn()
print(result)

#-------------------------------------------

def multiReturnFn():
    return "I'm Returning Function", 2

result2 = multiReturnFn() # ("I'm Returning Function", 2)
print(result2)

#-------------------------------------------

def paramFn(a):
    print(a)

paramFn("This is Me!")

#-------------------------------------------

def default_paramFn(a, b = 2, c = 3):
    return a + b + c

output = default_paramFn(1)
print(output)

#-------------------------------------------

def outer(a):

    def nested(b):
        return b  * a
    a = nested(a)
    return a

print(outer(4))
# 
#-------------------------------------------

def f(a):
    def g(b):
        return a * b
    return g

print(f(3)(2))

#-------------------------------------------

def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g

print(f(3)(2)(4))

#-------------------------------------------
# Recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#-------------------------------------------
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

def tail_sum(n, accumulator = 0):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n - 1, accumulator + n)

print(sum(10))
print(tail_sum(10))

#-------------------------------------------

# Lamda functions:
f = lambda a, b: a+b
print(f(1,2))

f = lambda a: lambda b: lambda c: a * b * c
print(f(5)(4)(3))

f = lambda c: lambda a, b: lambda d: (c * (a + b)) % d
print(f(2)(3, 4)(11))