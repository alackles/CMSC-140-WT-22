# Numbers

my_first_variable = 9
print(my_first_variable)

decimal = 2.3
print(decimal)

classname = "Intro to Python"
print(classname)

print(my_first_variable + decimal)
added = my_first_variable  + decimal
print(added)

# won't work: sentence = classname + 140
sentence = classname + " " + str(140)
print(sentence)
x = 7
print(x)
print(x == 7)

a = int("49284924")
print(a + 10)

# can't do this:
#b = int("apples")
#print(b + 10)

#age = input("Enter your age: ")
#print("Your age is " + age)
#numerical_age = int(age)
#next_age = numerical_age + 1
#print("Next year you will be " + str(next_age))
#print(age, numerical_age)

# input an integer 
#my_int = int(input())

my_bool = True
print(my_bool)

print(True or False)
print("Example: ")
print(2 < 3 or 3 > 100)
a = 2 < 3
print(a)

# equality checks
eq = 5 == 5
neq = 4 != 5
print(eq, neq)

i = 0
if i == 0:
    j = 0
    i += 20 # same as i = i + 20
    j  = j + 7
    print("Hello")
    print(i, j)
elif i == 20:
    print("Hello again")
else:
    print("i is", i)

answer = input("Are you a CS major?: ")
if answer == "yes":
    print("Welcome to CMSC!")
elif answer == "no":
    print("Ok. I hope you enjoy your major!")
else:
    print("Sorry, didn't understand.")

class_code = 500
if class_code == 140:
    print("This is Python Programming.")
elif class_code == 150:
    print("This is Java Programming.")
elif class_code == 270:
    print("This is Data Structures.")
elif class_code >= 200:
    print("This is an upper-level class.")
elif class_code >= 400: 
    print("This is an advanced class.")
