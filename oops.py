# Object Oriented programming
'''
hiding information
encapsulation
inheritance
polymorphism
'''

# Class: a collection of attributes that are defined for any object data member, methods

import math

class Complex:
    'this class simulates complex numbers'
    def __init__(self, real = 0, imaginary = 0):
        if (type(real) not in (int, float)) or (type(imaginary) not in (int, float)):
            raise Exception("Args are not an int or float")
        self.__real = real
        self.__imaginary = imaginary
    
    def GetReal(self):
        return self.__real
    
    def GetImaginary(self):
        return self.__imaginary
    
    def GetModulus(self):
        return math.sqrt(self.GetReal()*self.GetReal() + self.GetImaginary()*self.GetImaginary())
    
    def GetPhi(self):
        return math.atan2(self.GetImaginary(), self.GetReal())

    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception("real must be int or float value")
        self.__real = val
    
    def SetImaginary(self, val):
        if type(val) not in (int, float):
            raise Exception("real must be int or float value")
        self.__imaginary = val

    def __str__(self):
        return str(self.GetReal()) + "+" + str(self.GetImaginary()) + "i"

    def __add__(self, other):
        return Complex(self.GetReal() + other.GetReal(), self.GetImaginary() + other.GetImaginary())

    def __mul__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() * other, self.GetImaginary() * other)
        else:
            return Complex(self.GetReal() * other.GetReal() - self.GetImaginary() * other.GetImaginary(), self.GetImaginary() * other.GetImaginary() + self.GetReal() * other.GetReal())
    
    def __truediv__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() / float(other), self.GetImaginary() / float(other))
        else:
            a, b, c, d = self.GetReal(), self.GetImaginary(), other.GetReal(), other.GetImaginary()
            nominator = c * c + d * d
            return Complex((a*c + b*d) / nominator, (b*c - a*d) / nominator)



c = Complex(1, 1)
print(c.real, c.imaginary)
c = Complex(2)
print(c.real, c.imaginary)

try:
    c = Complex((1, 2, 3), [1, 2, 3])
    print(c.real, c.imaginary)
except Exception as e:
    print(e)

# methods: special functions inside the body of the class

try:
    c = Complex(1, 2)
    print(c.GetReal(), c.GetImaginary())
except Exception as e:
    print(e)

try:
    c = Complex()
    c.SetReal((3, 2))
    c.SetImaginary((5, 4))
    print(c.GetReal(), c.GetImaginary())
except Exception as e:
    print(e)

c = Complex(-2, 4)
print(c.GetModulus(), c.GetPhi()) # 4.47213595499958 2.0344439357957027

# Operator Overloading:

a = Complex(-3, 4)
b = Complex(5, 6)
print(a + b) # 2+10i
print(a * 2) # -6+8i
print(a * b) # -39+9i
print(a / 2) # -1.5+2.0i
print(a / b) # 0.14754098360655737+0.6229508196721312i

# Class Inheritance:

class Vehicle:
    def __init__(self, VIN, weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
    
    def GetWeight(self):
        return self.weight

    def GetManufacturer(self):
        return self.manufacturer
    
    def VehicleType(self):
        pass

class Car(Vehicle):
    def __init__(self, VIN, weight, manufacturer, seats):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.seats = seats
    
    def NumberOfSeats(self):
        return self.seats

    def VehicleType(self):
        return "Car"

class Truck(Vehicle):
    def __init__(self, VIN, weight, manufacturer, capacity):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.capacity = capacity
    
    def TransportCapacity(self):
        return self.capacity

    def VehicleType(self):
        return "TRUCK"

a = Car("ABS", 1000, "BMW", 4)
b = Truck("CDW", 1000, "MAN", 10000)
c = Car("SFR", 1000, "FORD", 4)
d = Truck("BGF", 1000, "MERCEDES", 15000)

print(a.GetWeight(), b.GetManufacturer(), c.NumberOfSeats(), d.TransportCapacity()) # 1000 MAN 4 15000

for v in [a, b, c, d]:
    print(v.GetManufacturer(), v.VehicleType())
'''
BMW Car
MAN TRUCK
FORD Car
MERCEDES TRUCK
'''

class Student(object):
    number_of_students = 0
    def __init__(self, name, index):
        self.name = name
        self.index = index
        Student.number_of_students += 1
    def __del__(self):
        Student.number_of_students -= 1  # destructor method

s1 = Student("Python", 123)
s2 = Student("JavaScript", 234)
print(Student.number_of_students, s1.number_of_students, s2.number_of_students) # 2 2 2

del s2
print(Student.number_of_students) # 1