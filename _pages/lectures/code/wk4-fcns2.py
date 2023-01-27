import math

print("Hi", end="")
print("Hello")

def cubed(n):
    #print(n*n*n)
    return n*n*n

def adder(x, y):
    mysum = x + y
    print(mysum)

adder(2, 4)
x = cubed(7)
print(x)

def f_to_c(f):
    c = (f-32)*(5/9)
    return round(c,0)


def intuitive_c(temp):
    if temp < 0:
        print("Freezing!")
    elif temp < 10: 
        print("Cold!")
    elif temp < 20:
        print("Warm!")
    elif temp < 30:
        print("Hot!")
    else:
        print("Scorching!") 

intuitive_c(27)

convert = f_to_c(75)
intuitive_c(convert)

intuitive_c(f_to_c(75))

def my_name(name):
    return "My name is " + name

my_name("Acacia")
print(my_name("Acacia"))

def plus_minus(a):
    return [a, -a]

print(plus_minus(20))

x = math.sqrt(25)
print(x)